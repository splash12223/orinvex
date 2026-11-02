import re
import sys
import time
from pathlib import Path


class OrinvexError(Exception):
    pass


class Orinvex:
    def __init__(self):
        self.variables = {}
        self.imports = set()

    def value(self, source):
        source = source.strip()

        if source == "<true>":
            return True
        if source == "<false>":
            return False

        if source.startswith('"') and source.endswith('"'):
            return source[1:-1]

        if source.startswith("'") and source.endswith("'"):
            return source[1:-1]

        if re.fullmatch(r"-?\d+", source):
            return int(source)

        if re.fullmatch(r"-?\d+\.\d+", source):
            return float(source)

        match = re.fullmatch(r"data:Get\.([A-Za-z_]\w*)", source)
        if match:
            name = match.group(1)
            if name not in self.variables:
                raise OrinvexError(
                    f"Variable '{name}' does not exist"
                )
            return self.variables[name]

        raise OrinvexError(f"Unknown value: {source}")

    def execute_command(self, command):
        command = command.strip()

        if not command or command.startswith("#"):
            return

        if command == "import rest":
            self.imports.add("rest")
            return

        # Variable declaration
        match = re.fullmatch(
            r"define\.([A-Za-z_]\w*)\s*=\s*(.*?)\.end",
            command
        )
        if match:
            name, raw_value = match.groups()

            if name in self.variables:
                raise OrinvexError(
                    f"Variable '{name}' is already defined"
                )

            self.variables[name] = self.value(raw_value)
            return

        # Console text
        match = re.fullmatch(
            r"print\.ConsoleText\((.*)\)end",
            command
        )
        if match:
            print(self.value(match.group(1)))
            return

        # Text intended for a game integration
        match = re.fullmatch(
            r"print\.Text\((.*)\)end",
            command
        )
        if match:
            raise OrinvexError(
                "print.Text() requires a game integration. "
                "Use print.ConsoleText() in the terminal."
            )

        # Number output
        match = re.fullmatch(
            r"print\.Number\((.*)\)end",
            command
        )
        if match:
            number = self.value(match.group(1))

            if isinstance(number, bool) or not isinstance(
                number, (int, float)
            ):
                raise OrinvexError(
                    "print.Number() requires a number"
                )

            print(number)
            return

        # Wait library
        match = re.fullmatch(
            r"rest\.wait\s*--\s*(time|milliseconds)\((.*?)\)end",
            command
        )
        if match:
            if "rest" not in self.imports:
                raise OrinvexError(
                    "Library 'rest' is not imported"
                )

            unit, raw_time = match.groups()
            duration = self.value(raw_time)

            if isinstance(duration, bool) or not isinstance(
                duration, (int, float)
            ):
                raise OrinvexError("Wait duration must be a number")

            if duration < 0:
                raise OrinvexError(
                    "Wait duration cannot be negative"
                )

            if unit == "milliseconds":
                duration /= 1000

            time.sleep(duration)
            return

        raise OrinvexError(f"Unknown command: {command}")

    def execute_lines(self, lines):
        index = 0

        while index < len(lines):
            line = lines[index].strip()
            index += 1

            if not line or line.startswith("#"):
                continue

            # Loop: loop -- <true>.Repeat(5)
            loop_match = re.fullmatch(
                r"loop\s*--\s*(<true>|<false>)\.Repeat\((\d+)\)",
                line
            )

            if loop_match:
                condition, count = loop_match.groups()
                count = int(count)
                body = []
                depth = 1

                while index < len(lines):
                    current = lines[index].strip()
                    index += 1

                    if re.fullmatch(
                        r"loop\s*--\s*(<true>|<false>)\.Repeat\(\d+\)",
                        current
                    ):
                        depth += 1

                    if current == "end":
                        depth -= 1
                        if depth == 0:
                            break

                    body.append(current)

                if depth != 0:
                    raise OrinvexError(
                        "Loop is missing its closing 'end'"
                    )

                if condition == "<true>":
                    for _ in range(count):
                        self.execute_lines(body)

                continue

            if line == "end":
                continue

            # Commands separated by " - "
            commands = re.split(r"\s+-\s+", line)

            for command in commands:
                self.execute_command(command)

    def run_file(self, filename):
        path = Path(filename)

        if not path.is_file():
            raise OrinvexError(
                f"File not found: {filename}"
            )

        source = path.read_text(encoding="utf-8")
        self.execute_lines(source.splitlines())


def main():
    if len(sys.argv) != 2:
        print("Orinvex interpreter")
        print("Usage: python3 orinvex.py program.ovx")
        sys.exit(1)

    interpreter = Orinvex()

    try:
        interpreter.run_file(sys.argv[1])
    except (OrinvexError, ValueError) as error:
        print(f"Orinvex error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

from dataclasses import dataclass


DIRECTIONS = ["N", "E", "S", "W"]

MOVE_MAP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Robot:
    x: int
    y: int
    direction: str
    lost: bool = False


def turn_left(direction: str) -> str:
    if direction not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")

    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index - 1) % 4]


def turn_right(direction: str) -> str:
    if direction not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")

    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index + 1) % 4]


def is_out_of_bounds(x: int, y: int, width: int, height: int) -> bool:
    return x < 0 or x > width or y < 0 or y > height


def execute_command(
    robot: Robot,
    command: str,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> Robot:
    if robot.lost:
        return robot

    if command == "L":
        return Robot(robot.x, robot.y, turn_left(robot.direction), robot.lost)

    if command == "R":
        return Robot(robot.x, robot.y, turn_right(robot.direction), robot.lost)

    if command == "F":
        dx, dy = MOVE_MAP[robot.direction]
        next_x = robot.x + dx
        next_y = robot.y + dy

        if is_out_of_bounds(next_x, next_y, width, height):
            scent_key = (robot.x, robot.y, robot.direction)

            if scent_key in scents:
                # 忽略這次 F，但不 LOST
                return Robot(robot.x, robot.y, robot.direction, False)

            scents.add(scent_key)
            return Robot(robot.x, robot.y, robot.direction, True)

        return Robot(next_x, next_y, robot.direction, False)
    raise ValueError(f"Invalid command: {command}")


def execute_commands(
    robot: Robot,
    commands: str,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> Robot:
    current_robot = robot

    for command in commands:
        current_robot = execute_command(current_robot, command, width, height, scents)
        if current_robot.lost:
            break

    return current_robot
import math
import sys
from dataclasses import replace

import pygame

from robot_core import Robot, execute_command


GRID_WIDTH = 5
GRID_HEIGHT = 3
CELL_SIZE = 120
MARGIN = 40
HUD_WIDTH = 320

WINDOW_WIDTH = MARGIN * 2 + (GRID_WIDTH + 1) * CELL_SIZE + HUD_WIDTH
WINDOW_HEIGHT = MARGIN * 2 + (GRID_HEIGHT + 1) * CELL_SIZE

FPS = 60
REPLAY_STEP_MS = 500

BG_COLOR = (245, 247, 250)
GRID_COLOR = (180, 188, 196)
AXIS_COLOR = (120, 130, 140)
ROBOT_COLOR = (60, 120, 220)
LOST_COLOR = (220, 70, 70)
SCENT_COLOR = (230, 150, 40)
TEXT_COLOR = (30, 35, 40)
PANEL_COLOR = (255, 255, 255)
PANEL_BORDER = (210, 215, 220)
HELP_COLOR = (90, 95, 100)


def grid_to_screen(x: int, y: int) -> tuple[int, int]:
    """Convert grid coordinates to screen coordinates (center of cell)."""
    screen_x = MARGIN + x * CELL_SIZE
    screen_y = WINDOW_HEIGHT - MARGIN - y * CELL_SIZE
    return screen_x, screen_y


def direction_to_angle(direction: str) -> float:
    angles = {
        "N": -math.pi / 2,
        "E": 0,
        "S": math.pi / 2,
        "W": math.pi,
    }
    return angles[direction]


def create_default_robot() -> Robot:
    return Robot(0, 0, "N", False)


def clone_robot(robot: Robot) -> Robot:
    return replace(robot)


def clone_scents(scents: set[tuple[int, int, str]]) -> set[tuple[int, int, str]]:
    return set(scents)


def make_snapshot(
    robot: Robot,
    scents: set[tuple[int, int, str]],
    last_command: str,
    message: str,
) -> dict:
    return {
        "robot": clone_robot(robot),
        "scents": clone_scents(scents),
        "last_command": last_command,
        "message": message,
    }


def try_execute_command(
    robot: Robot,
    command: str,
    scents: set[tuple[int, int, str]],
) -> tuple[Robot, str]:
    try:
        updated = execute_command(robot, command, GRID_WIDTH, GRID_HEIGHT, scents)
    except ValueError as exc:
        return robot, f"指令錯誤：{exc}"

    if updated.lost:
        return updated, f"執行 {command}：機器人 LOST，已留下 scent"

    if updated.x == robot.x and updated.y == robot.y and updated.direction == robot.direction and command == "F":
        return updated, f"執行 {command}：因 scent 忽略危險前進"

    return updated, f"執行 {command}：成功"


def draw_grid(screen: pygame.Surface, font: pygame.font.Font) -> None:
    for x in range(GRID_WIDTH + 1):
        start = grid_to_screen(x, 0)
        end = grid_to_screen(x, GRID_HEIGHT)
        pygame.draw.line(screen, GRID_COLOR, start, end, 2)

    for y in range(GRID_HEIGHT + 1):
        start = grid_to_screen(0, y)
        end = grid_to_screen(GRID_WIDTH, y)
        pygame.draw.line(screen, GRID_COLOR, start, end, 2)

    for x in range(GRID_WIDTH + 1):
        label = font.render(str(x), True, AXIS_COLOR)
        label_pos = grid_to_screen(x, 0)
        screen.blit(label, (label_pos[0] - 6, WINDOW_HEIGHT - MARGIN + 8))

    for y in range(GRID_HEIGHT + 1):
        label = font.render(str(y), True, AXIS_COLOR)
        label_pos = grid_to_screen(0, y)
        screen.blit(label, (MARGIN - 22, label_pos[1] - 10))


def draw_scents(screen: pygame.Surface, scents: set[tuple[int, int, str]], font: pygame.font.Font) -> None:
    for x, y, direction in scents:
        center_x, center_y = grid_to_screen(x, y)
        pygame.draw.circle(screen, SCENT_COLOR, (center_x, center_y), 10)
        text = font.render(direction, True, TEXT_COLOR)
        screen.blit(text, (center_x + 12, center_y - 10))


def draw_robot(screen: pygame.Surface, robot: Robot) -> None:
    center_x, center_y = grid_to_screen(robot.x, robot.y)

    radius = CELL_SIZE // 4
    body_color = LOST_COLOR if robot.lost else ROBOT_COLOR
    pygame.draw.circle(screen, body_color, (center_x, center_y), radius)

    angle = direction_to_angle(robot.direction)
    tip = (
        center_x + int(math.cos(angle) * radius * 1.2),
        center_y + int(math.sin(angle) * radius * 1.2),
    )
    left = (
        center_x + int(math.cos(angle + 2.45) * radius * 0.9),
        center_y + int(math.sin(angle + 2.45) * radius * 0.9),
    )
    right = (
        center_x + int(math.cos(angle - 2.45) * radius * 0.9),
        center_y + int(math.sin(angle - 2.45) * radius * 0.9),
    )
    pygame.draw.polygon(screen, (255, 255, 255), [tip, left, right])

    if robot.lost:
        pygame.draw.line(screen, (255, 255, 255), (center_x - 20, center_y - 20), (center_x + 20, center_y + 20), 4)
        pygame.draw.line(screen, (255, 255, 255), (center_x - 20, center_y + 20), (center_x + 20, center_y - 20), 4)


def draw_panel(
    screen: pygame.Surface,
    title_font: pygame.font.Font,
    body_font: pygame.font.Font,
    small_font: pygame.font.Font,
    robot: Robot,
    scents: set[tuple[int, int, str]],
    last_command: str,
    message: str,
    replay_mode: bool,
    replay_index: int,
    replay_total: int,
) -> None:
    panel_x = MARGIN + (GRID_WIDTH + 1) * CELL_SIZE + 20
    panel_rect = pygame.Rect(panel_x, MARGIN, HUD_WIDTH - 40, WINDOW_HEIGHT - MARGIN * 2)

    pygame.draw.rect(screen, PANEL_COLOR, panel_rect, border_radius=12)
    pygame.draw.rect(screen, PANEL_BORDER, panel_rect, width=2, border_radius=12)

    y = panel_rect.top + 20

    def line(text: str, font_obj: pygame.font.Font, color=TEXT_COLOR, gap=10) -> None:
        nonlocal y
        surface = font_obj.render(text, True, color)
        screen.blit(surface, (panel_rect.left + 18, y))
        y += surface.get_height() + gap

    line("Mars Robot Simulator", title_font, gap=16)
    line(f"Position : ({robot.x}, {robot.y})", body_font)
    line(f"Direction: {robot.direction}", body_font)
    line(f"State    : {'LOST' if robot.lost else 'ALIVE'}", body_font)
    line(f"Scents   : {len(scents)}", body_font)
    line(f"Last Cmd : {last_command or '-'}", body_font, gap=16)

    if replay_mode:
        line(f"Replay   : {replay_index + 1}/{replay_total}", body_font, (70, 100, 180), gap=16)

    line("訊息：", body_font, gap=6)
    for msg_line in wrap_text(message or "等待輸入指令", 24):
        line(msg_line, small_font, HELP_COLOR, gap=4)

    y += 14
    line("操作鍵：", body_font, gap=8)
    help_lines = [
        "L / R / F : 執行一步",
        "N         : 新機器人",
        "C         : 清除 scent",
        "G         : 回放歷程",
        "SPACE     : 暫停/繼續回放",
        "ESC       : 離開",
    ]
    for help_line in help_lines:
        line(help_line, small_font, HELP_COLOR, gap=6)


def wrap_text(text: str, max_chars: int) -> list[str]:
    if not text:
        return [""]

    lines: list[str] = []
    current = ""

    for ch in text:
        current += ch
        if len(current) >= max_chars:
            lines.append(current)
            current = ""

    if current:
        lines.append(current)

    return lines


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Mars Robot Simulator")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 28, bold=True)
    body_font = pygame.font.SysFont("arial", 24)
    small_font = pygame.font.SysFont("arial", 20)

    robot = create_default_robot()
    scents: set[tuple[int, int, str]] = set()
    last_command = ""
    message = "歡迎開始。使用 L / R / F 操作機器人。"

    history: list[dict] = [make_snapshot(robot, scents, "", "初始狀態")]
    replay_mode = False
    replay_index = 0
    replay_paused = False
    replay_last_tick = pygame.time.get_ticks()

    running = True
    while running:
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

                if event.key == pygame.K_SPACE and replay_mode:
                    replay_paused = not replay_paused
                    continue

                if event.key == pygame.K_g:
                    if history:
                        replay_mode = True
                        replay_index = 0
                        replay_paused = False
                        replay_last_tick = now
                        message = "開始回放歷程。按 SPACE 可暫停/繼續。"
                    continue

                if replay_mode:
                    continue

                if event.key == pygame.K_n:
                    robot = create_default_robot()
                    last_command = "N"
                    message = "已建立新機器人，保留既有 scent。"
                    history.append(make_snapshot(robot, scents, last_command, message))
                    continue

                if event.key == pygame.K_c:
                    scents.clear()
                    last_command = "C"
                    message = "已清除所有 scent。"
                    history.append(make_snapshot(robot, scents, last_command, message))
                    continue

                key_map = {
                    pygame.K_l: "L",
                    pygame.K_r: "R",
                    pygame.K_f: "F",
                }

                if event.key in key_map:
                    command = key_map[event.key]
                    robot, message = try_execute_command(robot, command, scents)
                    last_command = command
                    history.append(make_snapshot(robot, scents, last_command, message))

        if replay_mode and history:
            if not replay_paused and now - replay_last_tick >= REPLAY_STEP_MS:
                replay_last_tick = now
                replay_index += 1
                if replay_index >= len(history):
                    replay_index = len(history) - 1
                    replay_mode = False
                    message = "回放結束，已返回即時模式。"

        if replay_mode and history:
            state = history[replay_index]
            display_robot = state["robot"]
            display_scents = state["scents"]
            display_last_command = state["last_command"]
            display_message = state["message"]
        else:
            display_robot = robot
            display_scents = scents
            display_last_command = last_command
            display_message = message

        screen.fill(BG_COLOR)
        draw_grid(screen, small_font)
        draw_scents(screen, display_scents, small_font)
        draw_robot(screen, display_robot)
        draw_panel(
            screen,
            title_font,
            body_font,
            small_font,
            display_robot,
            display_scents,
            display_last_command,
            display_message,
            replay_mode,
            replay_index,
            len(history),
        )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
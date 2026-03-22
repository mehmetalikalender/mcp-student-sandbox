from typing import Iterable, List


TAX_MULTIPLIER = 1.15


def calculate_total(value: float, multiplier: float = TAX_MULTIPLIER) -> float:
    """Calculate a single total value using the provided multiplier."""
    return value * multiplier


def format_total_line(total: float) -> str:
    """Return a user-friendly total line."""
    return f"Total: {total:.2f}"


def append_results_to_log(results: List[float], log_path: str = "log.txt") -> None:
    """Append calculated results to the log file."""
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(f"{results}\n")


def process_data(data: Iterable[float]) -> List[float]:
    """Process input values by applying a multiplier, printing, and logging results."""
    results: List[float] = []

    for item in data:
        total = calculate_total(item)
        print(format_total_line(total))
        results.append(total)

    append_results_to_log(results)
    return results

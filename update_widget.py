import datetime
import json
import os.path


def get_day_of_year(ref: datetime.datetime) -> int:
    return ref.toordinal() - datetime.date(ref.year, 1, 1).toordinal() + 1


def main():
    widget_json_file_path = os.path.join(
        os.path.dirname(__file__),
        "widget.json"
    )

    with open(widget_json_file_path, "r") as f:
        widget = json.load(f)

    now = datetime.datetime.now()
    day_of_year = min(get_day_of_year(now), 365)  # hehe

    data = widget["data"]

    data["year"] = str(now.year)
    data["pie_chart"] = f"https://raw.githubusercontent.com/chowder/year-progress-widget/main/images/{day_of_year}.png"
    data["percentage"] = f"{int((day_of_year / 365) * 100)}%"

    with open(widget_json_file_path, "w") as f:
        json.dump(widget, f, indent=2)


if __name__ == "__main__":
    main()

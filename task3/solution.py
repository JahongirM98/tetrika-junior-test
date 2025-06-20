def to_intervals(times: list[int]) -> list[tuple[int, int]]:
    return [(times[i], times[i + 1]) for i in range(0, len(times), 2)]


def clip_to_lesson(intervals, lesson):
    return [
        (max(start, lesson[0]), min(end, lesson[1]))
        for start, end in intervals
        if end > lesson[0] and start < lesson[1]
    ]


def intersect(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    if start < end:
        return (start, end)
    return None


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # пересекаются
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals["lesson"]
    pupil = clip_to_lesson(to_intervals(intervals["pupil"]), lesson)
    tutor = clip_to_lesson(to_intervals(intervals["tutor"]), lesson)

    intersections = []
    for p in pupil:
        for t in tutor:
            iv = intersect(p, t)
            if iv:
                intersections.append(iv)

    merged = merge_intervals(intersections)
    return sum(end - start for start, end in merged)

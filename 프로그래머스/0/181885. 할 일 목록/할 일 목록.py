def solution(todo_list, finished):
    return [todo_list[idx] for idx, val in enumerate(finished) if not val]
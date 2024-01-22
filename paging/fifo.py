order = [17, 12, 9, 14, 8, 5, 1, 19, 17, 16, 15, 5, 9, 18, 9, 4, 5, 4, 9, 12, 15, 5, 9, 14, 10, 
6, 13, 1, 7, 12, 16, 12, 13, 19, 10, 16, 13, 16, 1, 19, 10, 9, 7, 19, 7, 4, 17, 9, 2]

ram_frames = []
limit_frames = 3

swap_cnt = 0

def exists(arr: [], el: int) -> bool:
    for i in arr:
        if i == el:
            return True
    return False

def print_state(i: int, arr: [], el_queued: [], el_in: [] = [], el_out: [] = []):
    i += 1
    print(f"{i})\t {el_queued} \t--->\t {arr}, \tin: {el_in}, out: {el_out}")


for i in range(len(order)):
    if len(ram_frames) < limit_frames:
        ram_frames.append(order[i])
        print_state(i, ram_frames, [order[i]], el_in=[order[i]])
        swap_cnt += 1
        continue
    if exists(ram_frames, order[i]):
        print_state(i, ram_frames, [order[i]])
        continue
    else:
        to_remove = ram_frames.pop(0)
        ram_frames.append(order[i])
        swap_cnt += 1
        print_state(i, ram_frames, [order[i]], [order[i]], [to_remove])

print("Количество замен:", swap_cnt)

    
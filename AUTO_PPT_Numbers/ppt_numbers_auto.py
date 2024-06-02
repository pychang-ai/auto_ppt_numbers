def generate_step_strings(total_steps):
    step_strings = []
    for i in range(1, total_steps + 1):
        step_strings.append(f"({i}/{total_steps})")
    return step_strings

def save_to_markdown(step_strings, filename="steps.md"):
    with open(filename, 'w') as file:
        for step_string in step_strings:
            file.write(f"{step_string}\n")

# 示例使用
total_steps = 4  # 可以更改为所需的总步数
step_strings = generate_step_strings(total_steps)
save_to_markdown(step_strings)

print("Step strings saved to steps.md")

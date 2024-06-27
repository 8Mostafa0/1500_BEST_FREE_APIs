from main import get_data


data = get_data()


orders = {}

for d in data:
    title = d[0]
    desc = d[1]
    link = d[2]
    
    if orders.get(d[3]) is not None:
        orders[d[3]] += list([d])
    else:
        orders[d[3]] = list([d])
with open('output.md', 'w', encoding='utf-8') as f:

    for topic in orders:
        f.write(f"\n\n# {topic}:\n\n")
        f.write("| Title | Description | Link |\n")
        f.write("| -------- | ------- | -------- |\n")
        for item in orders[topic]:
            f.write(f"| {item[0]} | {item[2]} | {item[1]} |\n")
            

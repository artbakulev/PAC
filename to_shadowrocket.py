INPUT_FILE = 'pac_decoded.txt'
OUTPUT_FILE = 'pac_shadowrocket.txt'
DEFAULT_ACTION = 'PROXY'
EXCEPTION_ACTION = 'DIRECT'

HOST_SECTION = [
    '[Host]',
    'localhost = 127.0.0.1',
]


def convert_line(line, default_action=DEFAULT_ACTION, exception_action=EXCEPTION_ACTION):
    line = line.strip()
    if not line or line.startswith('!') or line.startswith('[') or line.startswith('#'):
        return None

    if line.startswith('@@'):
        rule = line[2:]
        action = exception_action
    else:
        rule = line
        action = default_action

    if rule.startswith('||'):
        domain = rule[2:]
        typ = 'DOMAIN-SUFFIX'
    elif rule.startswith('|') and not rule.startswith('||'):
        domain = rule[1:]
        typ = 'DOMAIN'
    else:
        domain = rule.lstrip('.')
        typ = 'DOMAIN-SUFFIX'

    domain = domain.split('/')[0]

    return f"{typ},{domain},{action}"


def main():
    out_lines = HOST_SECTION + ['','[Rule]']

    with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
        for raw in infile:
            conv = convert_line(raw)
            if conv:
                out_lines.append(conv)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(out_lines))

    print(f"Converted rules written to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()

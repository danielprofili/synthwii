import mido
import time
import os, sys, json

CFG_PATH = os.path.join(sys.path[0], 'config.json')

def setup_midi():
    cfg = load_config()
    if cfg is not None:
        return cfg['interface']

    outputs = mido.get_output_names()
    if len(outputs) == 0:
        print('Error: no MIDI outputs found!')
        exit(0)

    print('Select a MIDI output port: ')
    for i in range(len(outputs)):
        print('(%d) %s' % (i, outputs[i]))

    while True:
        print('(0 - %d): ' % (len(outputs) - 1), end='')
        try:
            ans = int(input())
        except ValueError:
            print('Not a number')
            continue

        if ans < 0 or ans >= len(outputs):
            print('Invalid choice')
        else:
            # write choice to config
            write_config('interface', outputs[ans])
            return outputs[ans]


def load_config():
    # check for configuration file
    if os.path.exists(CFG_PATH):
        with open(CFG_PATH) as f:
            cfg = json.load(f)
        return cfg
    else:
        # no config, so better make it
        print('Creating empty config file at %s' % CFG_PATH)
        with open(CFG_PATH, 'x') as f:
            json.dump({'interface' : ''}, f)
            return
            
def write_config(key, val):
    with open(CFG_PATH) as f:
        cfg = json.load(f)
    cfg[key] = val
    with open(CFG_PATH, 'w') as f:
        json.dump(cfg, f)

# main routine
if __name__ == '__main__':
    out_name = setup_midi()
    # print(out_name)
    with mido.open_output(out_name) as out:
        out.send(mido.Message('note_on', note=60))
        time.sleep(1)
        out.send(mido.Message('note_off', note=60))
        
    

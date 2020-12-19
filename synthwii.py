import mido
import time

def setup_midi():
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
            return outputs[ans]

# main routine
if __name__ == '__main__':
    out_name = setup_midi()
    # print(out_name)
    with mido.open_output(out_name) as out:
        out.send(mido.Message('note_on', note=60))
        time.sleep(1)
        out.send(mido.Message('note_off', note=60))
        
    

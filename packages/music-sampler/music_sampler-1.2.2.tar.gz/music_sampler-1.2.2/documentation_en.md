[TOC]

# Music Sampler

## Description

Music Sampler is a music player which associates each key on the keyboard to a
set of actions to run.

## Dependencies and installation

- You need ffmpeg installed. For that, you can use package `libav-tools` (debian):

        sudo apt-get install libav-tools

If you use the compiled version of Music Sampler (cf. below for a download
link), you need nothing else.

- To use sources, the following modules are required:

| module      | minimum version  | note                                                          |
| ----------- | ---------------- | ------------------------------------------------------------- |
| Cython      | 0.24             | to compile Kivy                                               |
| Kivy        | 1.9.1            | some features require to build/install with flag `USE_SDL2=1` |
| Markdown    | 2.6.6            | for documentation only                                        |
| pydub       | 0.16.4           |                                                               |
| Pygame      | 1.9.2.dev1       | used by Kivy                                                  |
| Pygments    | 2.1.3            | for documentation only                                        |
| sounddevice | 0.3.3            |                                                               |
| transitions | 0.4.1            |                                                               |
| PyYAML      | 3.11             |                                                               |

The project is also available via `pip`:

    pip install music_sampler

The program makes use of fonts "Symbola" and "Ubuntu" (Regular / Bold), that
must be available on your system, as well as the `portaudio` library:

    sudo apt-get install ttf-ancient-fonts ttf-ubuntu-font-family portaudio

Pour compiler kivy avec la librairie SDL2, il faut certains paquets installés:

    sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

cf [Installation
Kivy](https://kivy.org/docs/installation/installation-linux.html)

## Compiled version

A compiled version can be created with `pyinstaller`:

    :::bash
    pyinstaller music_sampler.spec

## Downloads

- An example configuration together with some music examples can be found on
  [owncloud](https://outils.immae.eu/owncloud/index.php/s/kSrIe15G1AiZ9YF)
- A precompiled version of `music_sampler` can also be found
  [in the same folder](https://outils.immae.eu/owncloud/index.php/s/kSrIe15G1AiZ9YF/download?path=%2F&files=music_sampler)
  (beware, it might not be up-to-date, please run the program with `-V` to see
  its corresponding version)

## Usage

The whole job consists in preparing all the transitions in the configuration
file `config.yml`.

The program should then be run in the folder in which the configuration file
lies (see below for an advanced use). A window with a keyboard appears. The
orange circle in the upper-right corner of the keyboard becomes green one every
music is loaded (or red in case of problem). A key is semi-transparent and
crossed when it is not usable at the moment: either because a music handled by
this key is not loaded yet (it may take some time when the program launches), or
because it has an action running.

An example configuration file is given with some keys and transitions. The
structure of the file (explained more in details below) should be easy to
understand just by looking at it.

### Possible actions

  - Clic on a key: shows the associated actions in the bottom-left block of the
    app.
  - Key stroke: if available, runs the actions associated to this key. When a
    key has currently running actions, his surround is black. Note that an
    action like "play a music" is almost instantaneous as it is considered
    "done" as soon as the music started playing.
    To prevent accidents in case of repeated stroke on a key, `Music Sampler`
    won't rerun the actions associated to that key if they are not already
    finished.
  - Ctrl+C or Ctrl+Q: leaves the program.
  - Ctrl+R: reloads the configuration file

### Options available at launch

All the options below are optional; usually, running the program in the correct
folder is enough

  * `-h, --help`: shows a list of available options
  * `-c CONFIG, --config CONFIG`: gives the configuration file to load (by
    default, `config.yml` in the current folder).
  * `-p MUSIC_PATH, --music-path MUSIC_PATH`: gives the path to find the musics
    (by default, the current folder)
  * `-d, --debug`: show debug informations in the terminal (disabled by default)
  * `-V, --version`: show current version and exit (only for the compiled
    version)
  * `-L, --language`: change application language. Current languages: fr, en
    (default 'fr')
  * `--no-focus-warning`: don't show warning when focus gets lost.

The following options are reserved for a more advanced use of Music Sampler, or
in case of problem with the standard configuration:

  * `-m, --builtin-mixing`: make the sound mixing locally. By default, Music
    Sampler will let the system do it and open one channel per music loaded. Use
    it only if the system cannot handle it.
  * `-l LATENCY, --latency LATENCY`: "low", "high" or a number of seconds
    (default "high")
  * `-b BLOCKSIZE, --blocksize BLOCKSIZE`: Number of frames for each mixing
    step. 0 (default) lets the program choose.
  * `-f FRAME_RATE, --frame-rate FRAME_RATE`: default 44100Hz
  * `-x CHANNELS, --channels CHANNELS` : Number of channels per music (default
    2, for stereo)
  * `-s SAMPLE_WIDTH, --sample-width SAMPLE_WIDTH`: number of bytes per frame
    (default 2).
  * `--device DEVICE` : select another sound device.
  * `--list-devices` : list available sound devices.
  * `-- ARGS` : arguments for Kivy library.

## Configure keys

**Warning: the format of the configuration file is still a work in progress and
may change without ensuring backward compatibility**

The file `config.yml` uses yaml syntax. Categories and sub-categories are
handled by space indentations (no tabs). Symbol `#` may be used for comments.

In case of error in the configuration file, an error message will show up.
Depending on its severity, Music Sampler may try to continue (ignoring
corresponding problems) or abort.

The file contains several sections:

    :::yaml
    aliases:
      ...

    music_properties:
      ...

    key_properties:
      ...

    keys:
      ...


### `music_properties`

This section lets you define global properties for the musics.

#### Examples

    :::yaml
      "music1.mp3":
        name: My favorite music
        gain: 1.4
Music "music1.mp3" is named "My favorite music". She is loaded at 140% of its
normal volume.

    :::yaml
      "music2.mp3":
        gain: 0.7

Music "music2.mp3" is loaded at 70% of its normal volume.

#### List of available options
- `name: My music` User-friendly name of the music, used in the interface
  instead of the filename.

- `gain: x` Loads the music with that initial gain x. This lets you equalize all
  your music at desired level, independently of the volume afterwards.

### `key_properties`: drawing and properties of keys

This section lets you describe the drawing of the key: color, description. By
default, a key assigned to one or more actions is shown in green

#### Examples

    :::yaml
      'ESC':
        description:
          - 
          - STOP!
        color: [255, 0, 0]
        repeat_delay: 2

The "esc" key is red, and text "STOP!" is shown on the second line. The key is
protected for 2 seconds after each stroke.

#### List of availale options
- `description`: the text on the key. Each item is shown on a line (no automatic
  line break). First line is shown just next to the "key" name and is in bold.
  On a standard screen, you may have about 3 lines visible (including the first
  one)
- `color: [r, g, b]`: the key color. r, g and b are the proportions respectively
  of red, green and blue, and each value must be between 0 and 255
- `repeat_delay: x` (default 0) : protection delay. Once all its actions are
  done, the key will remain disabled (semi-transparent and crossed) for that
  amount of time (in seconds).

### `keys` : actions related to keys

This section lets you describe for each key, the list of actions associated to
it. Note that except for `wait` and some particular cases (see below), all the
actions are almost instantaneous.


#### Examples

    :::yaml
    'a':
      - play: 
          file: "music1.mp3"
          volume: 70
          start_at: 10
      - wait:
          duration: 5
      - stop:
          file: "music1.mp3"
          fade_out: 2

Runs music "music1.mp3" at 70% of its maximum volume, at 10 seconds from the
start, then stops the music 5 seconds later with a 2 seconds fade out.

    :::yaml
    'b':
      - stop: 
          file: "music1.mp3"
          fade_out: 5
          wait: false
      - play:
          file: "music2.mp3"
          fade_in: 5

Make a cross fade of 5 seconds between "music1.mp3" and "music2.mp3"

    :::yaml
    'c':
      - stop: 
          file: "music1.mp3"
          fade_out: 5
          wait: true
      - wait:
          duration: 2
      - play:
          file: "music2.mp3"
      - seek:
          file: "music2.mp3"
          delta: false
          value: 60
Stops music "music1.mp3" with a 5 seconds fade out, waits for the end of the
fade out, plus 2 seconds, and then runs "music2.mp3" skipping the first minute.

    :::yaml
    'd':
      - volume: 
          file: "music1.mp3"
          value: 50
      - play:
          file: "noise.mp3"
          loop: 1
      - wait:
          file: "noise.mp3"
      - volume:
          file: "music1.mp3"
          value: 100

Lower volume of "music1.mp3" while "noise.mp3" is played above it (twice). Then
the volume of the music comes back to normal.

    :::yaml
    'e':
      - pause:
          file: "music1.mp3"
      - wait: 
          duration: 10
      - unpause:
          file: "music1.mp3"
      - seek:
          file: "music1.mp3"
          delta: true
          value: 5

Pauses "music1.mp3" for 10 seconds and reruns it afterward, seeking to 5 seconds
later.

#### List of all the actions:
- `play` : start a music. Music Sampler only runs a music once (if you want to
  have it playing several time concurrently, duplicate it or make symbolic
  link). Parameters:
    * `file: "music.mp3"` gives the played music (relative path).
    * `fade_in: x` (optional) runs the music with x seconds fade in.
    * `volume: x` (optional, default 100) sets the volume of the music.
    * `loop: x` (optional, default 0) music should be repeated x times. Indicate
      -1 for infinite loop. Note: x is the number of repetitions, thus the music
      is actually played x+1 times.
    * `start_at: x` (optional, default 0) start music skipping the first x
      seconds.
    * `restart_if_running: true/false` (optional, default false) if the music is
      already running, stop it and restart it.
- `stop` : stops a given music. Parameters:
    * `file: "music.mp3"` (optional) gives the music to stop. If no music is
      given, stops all of them.
    * `fade_out: x` (optional) stops music with a x seconds fade out.
    * `wait: true/false` (optional, default: false) when stopping with a fade
      out, wait for the fade to finish before continuing to the next actions. If
      the music stops naturally before the en of the fade out, the wait stops
      there too. When several musics are stopped in fade out, the `wait` only
      waits for the last one in the playlist (which can finish naturally before
      the others).
    * `set_wait_id: name` (optional, useless when `wait` is false) sets an id
      `name` to the wait (see `interrupt_wait`). Any valid string may be used.
- `volume` : change the volume of a given music. Parameters:
    * `file: "music.mp3"` (optional) which music to change. If no music is
      given, the global volume is changed.
    * `delta: true/false` (optional, default false) add/remove to the volume
      instead of setting an absolute value.
    * `value: x` if delta is false, sets the volume to x%. Note that this factor
      is applied to the music already loaded (with the initial gain). If delta
      is true, adds or remove the percentage to the current volume.
    * `fade: x` (optional) the volume change is applied with a x seconds fade.
- `pause` : pause a music. Parameters:
    * `file: "music.mp3"` (optional) gives the music to pause. If no music is
      given, it applies to all playing musics.
- `unpause` : unpause a music. Parameters:
    * `file: "music.mp3"` (optional) gives the msuic to unpause. If no music is
      given, it applies to all paused musics.
- `wait` : wait for some time or for an event. Parameters:
    * `file: "music.mp3"` (optional) wait for the end of music "music.mp3"
    * `duration: x` (optional) wait x seconds. If `file` and `duration` are
      given, wait the end of the music PLUS the `duration`.
    * `set_wait_id: name` (optional) gives an id to the wait event (see
      `interrupt_wait`). The id can be any valid string.
Note again that this action is one of the only action that is not almost
instantaneous. Use it wherever you need to make some time adjustments for other
actions.
- `seek` : seek to a specific position in a music. Parameters:
    * `file: "music.mp3"` (optional) gives the music to seek. If no music is
      given, applies to all playing musics.
    * `delta: true/false` (optional, default false) If `delta` is true, the time
      seek is relative. Otherwise, it is absolute.
    * `value: x` If `delta` is true, then moves the music forward or backward by
      x seconds. If delta is false, the music goes to that position. If the
      music is fading (fade in or volume fade), the effect is immediately
      interrupted. If the music is fading out, the "seek" is ignored. In case of
      `loop`, a relative seek may jump to previous or next loop if possible,
      while an absolute seek will jump to a position in the current loop.
- `stop_all_actions:` Interrupts all the running and pending actions. Note that
  a started music (even with a `loop` option) is the result of an action that is
  already finished and thus will keep playing (see `stop` for that). Parameters:
    * `other_only: true/false` (optional, default false): if `other_only` is
      true, the interruption is valid for all keys except the one that ran the
      action. When false, it is thus useless to add actions after that one.
- `interrupt_wait`: stop a wait event (normal `wait` or fade out wait). The keys
  that were waiting will move to the next actions. Parameters:
    * `wait_id: name` : gives the id of the `wait` to interrupt (defined with
      `set_wait_id`, see actions `wait` and `stop`). To interrupt several waits,
      use the same action several times.
- `run_command` : Run a command. Parameters:
    * `command: my_command` : Gives the command to run.
    * `wait: true/false` (optional, default false) if true, waits for the
      command to finish (this wait is not interruptible by interrupt_wait)

### `aliases` : define aliases

It is possible to define some aliases for the parameters. Those aliases are
internal to the configuration file. To give a nice name to a music, see
"music_properties".

The aliases syntax is the following:

    :::yaml
    aliases:
      alias1:
        param: value
      alias2:
        param1: value1
        param2: value2

You can then use in other places of the configuration file a special argument
`include: alias1` or `include: [alias1, alias2]` instead of `param: value`. In
the case of several aliases that have identical elements, only the last one is
kept. In all cases, a value defined outside of an include takes precedence. See
below examples.

#### Examples

    :::yaml
    aliases:
      music1:
        file: "path/to/my/favourite/music.mp3"

    keys:
      'a':
        play:
          include: music1

`music1` is now an alias for `file: "path/to/my/favourite/music.mp3"`. You can
use `include: music1` at any place where you would have written `file:
"path/to/my/favourite/music.mp3"`. Aliases cannot be used in section
"music_properties".

    :::yaml
    aliases:
      blue:
        color: [0, 0, 255]

    keys_properties:
      'a':
        description:
          - 
          - blue key
        include: blue

`blue` is an alias for color `[0, 0, 255]`. Wherever you need to specify `color:
[0, 0, 255]`, you may write `include: blue` instead.

    :::yaml
    aliases:
      long_time:
        duration: 42

    keys:
      'b':
        wait:
          include: long_time
        play: 
          file: "music1.mp3"

`long_time` is an alias for a 42 seconds duration. Instead of `duration: 42`,
you may use `include: long_time`.

## Troubleshooting

You'll find below a list of possible problems, and a possible solution. If you
find some other problems, please contact the author.

* The program starts and stops immediately.

It is usually a syntax error in the config file. In that case, the terminal
should give some informations.

* The music sizzles

It may be a latency problems (with slow computers). Try to adapt it to a higher
value (~0.1 seconds)

* Impossible to play more than one music at a time.

The system cannot mix the musics by itself. You may have a look at the device
list (`--list-devices`) and choose another. You may also try the integrated
mixer, but the result may not be very fluid (you will certainly need to adjust
blocksize and latency parameters if you do that)

If your system uses PulseAudio, it may be a configuration problem for the ALSA
plugin. In that case, try to put the following configuration in
`/etc/asound.conf` and restart your system. This is an empirical solution that
seems to have worked, there is no garanty that it will!

    pcm.!default {
      type pulse
      fallback "sysdefault"
      hint {
        show on
        description "Default ALSA Output (currently PulseAudio Sound Server)"
      }
    }

    ctl.!default {
      type pulse
      fallback "sysdefault"
    }

* The terminal shows an error:

        Exception in thread Thread-1:
        Traceback (most recent call last):
          File "threading.py", line 914, in _bootstrap_inner
          File "threading.py", line 862, in run
          File "kivy/input/providers/mtdev.py", line 219, in _thread_run
          File "kivy/lib/mtdev.py", line 131, in __init__
        PermissionError: [Errno 13] Permission denied: '/dev/input/event6'

This is a device permission error. It can be safely ignored.

* For other problems or bug, please see [Bug
  Tracker](https://git.immae.eu/mantisbt/view_all_bug_page.php?project_id=1&sort=status%2Clast_updated&dir=ASC%2CDESC)

## About

The musics in the examples come from [Jamendo](https://jamendo.com). The
complete version of those musics are available for free for a non-commercial
use:

[Short Blues](https://www.jamendo.com/track/340173/short-blues)

[To the Fantasy war](https://www.jamendo.com/track/778560/to-the-fantasy-war)

The crocodile noise comes from
[Universal-Soundbank](http://www.universal-soundbank.com/).

This program was developped originaly to help handling music for shows of the
circus company [Les pieds jaloux](http://piedsjaloux.fr/). With no available
sound manager, the artists sometimes had to run from the scene to make the sound
transitions, making as little interaction as possible with the computed (one
key).

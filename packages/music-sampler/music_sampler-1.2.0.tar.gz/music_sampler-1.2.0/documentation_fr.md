[TOC]

# Music Sampler

## Description

Music Sampler est un lecteur de musique qui permet de pré-programmer des transitions musicales, qui peuvent ensuite être lancées à l'aide d'un simple appui sur une touche.

## Pré-requis et installation

- Il faut avoir ffmpeg d'installé. Pour cela, il faut installer le paquet `libav-tools` :

        sudo apt-get install libav-tools

Si vous utilisez la version compilée de Music Sampler (cf. plus bas pour un lien de téléchargement), il n'y a rien d'autre à installer.

- Pour utiliser les sources directement, les modules suivants sont requis:

| module      | version minimale | commentaire                                                                 |
| ----------- | ---------------- | --------------------------------------------------------------------------- |
| Cython      | 0.24             | pour compiler Kivy                                                          |
| Kivy        | 1.9.1            | certaines fonctionnalités nécessitent de compiler/installer avec USE_SDL2=1 |
| Markdown    | 2.6.6            | pour la documentation uniquement                                            |
| pydub       | 0.16.4           |                                                                             |
| Pygame      | 1.9.2.dev1       | utilisée par Kivy                                                           |
| Pygments    | 2.1.3            | pour la documentation uniquement                                            |
| sounddevice | 0.3.3            |                                                                             |
| transitions | 0.4.1            |                                                                             |
| PyYAML      | 3.11             |                                                                             |

Le projet est également disponible via pip:

    pip install music_sampler

Le programme utilise les polices "Symbola" et "Ubuntu" (Regular / Bold), qui doivent être disponibles, et la librairie portaudio:

    sudo apt-get install ttf-ancient-fonts ttf-ubuntu-font-family portaudio

Pour compiler kivy avec la librairie SDL2, il faut certains paquets installés:

    sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

cf [Installation Kivy](https://kivy.org/docs/installation/installation-linux.html)

## Version compilée

Une version compilée peut être créée avec pyinstaller:

    :::bash
    pyinstaller music_sampler.spec

## Téléchargements

- Un exemple de configuration ainsi que des musiques associées à l'exemple peuvent être trouvées sur [owncloud](https://outils.immae.eu/owncloud/index.php/s/kSrIe15G1AiZ9YF)
- Une version précompilée de `music_sampler` peut également être téléchargée [dans le même dossier](https://outils.immae.eu/owncloud/index.php/s/kSrIe15G1AiZ9YF/download?path=%2F&files=music_sampler) (attention, elle n'est pas toujours forcément à jour, lancer le programme avec `-V` pour voir la version compilée)

## Utilisation

Tout le travail consiste à préparer les transitions dans le fichier de configuration config.yml.

Lancer ensuite le programme dans le dossier où se situe le fichier de configuration (voir plus bas pour une utilisation avancée). Une fenêtre représentant un clavier apparaît. Le rond orange dans le coin du clavier devient vert lorsque tout est chargé, ou rouge en cas de problème. Une touche grisée et barrée représente une touche non-utilisable pour le moment : soit parce que la musique est en cours de chargement (au lancement du programme, cela peut prendre un peu de temps sur certaines machines), soit parce qu'il y a une action en cours.

Un exemple de fichier de configuration est fourni, avec un certain nombre de touches et de transitions programmées (pour les trois musiques fournies), la syntaxe du fichier (expliquée plus bas) se comprend aisément en le regardant. De plus, certaines touches (par exemple 'ÉCHAP' pour tout arrêter) peuvent être gardées d'une fois sur l'autre.

### Actions possibles

  - Cliquer sur une touche : affiche les actions associées à cette touche (dans le cadre en bas à gauche).
  - Appuyer sur une touche : déclenche les actions associées à cette touche (affichées également dans le cadre en bas à gauche). Lorsqu'une touche a des actions en cours, son cadre est noir. Notez qu'une action de type "jouer une musique" est considérée comme terminée quand ladite musique est lancée. 
En cas d'appui répété sur une touche, music_sampler ne relance pas les actions associées à cette touche si ces actions ne sont pas terminées ; cela pour éviter les "accidents".
  - Ctrl+C ou Ctrl+Q : quitte le programme (possible aussi en cliquant simplement sur la croix en haut à droite).
  - Ctrl+R : recharge le fichier de configuration.

### Options disponibles au lancement

Toutes les options au lancement sont facultatives ; la plupart du temps lancer le programme dans le bon dossier suffit.

  * `-h, --help` : affiche une liste des options disponibles.
  * `-c CONFIG, --config CONFIG` : précise le fichier de configuration à charger (par défaut, config.yml qui se trouve dans le dossier où est lancé music_sampler).
  * `-p MUSIC_PATH, --music-path MUSIC_PATH` : précise le chemin des musiques (par défaut, le dossier courant).
  * `-d, --debug` : Affiche les informations de déboggage (désactivé par défaut)
  * `-V, --version` : affiche la version courante et quitte (utilisable uniquement pour la version compilée).
  * `-L, --language` : change la langue de l'application. Actuellement: fr, en (par défaut 'fr')
  * `--no-focus-warning`: Ne pas afficher d'avertissement lorsque l'application perd le focus.

Les options suivantes sont plutôt réservées à un usage avancé de music_sampler, ou en cas de problème avec la configuration standard :

  * `-m, --builtin-mixing` Effectue en interne le mixage des sons. Par défaut, music_sampler confie le mixage au système : n'activer cette option que si le système n'y parvient pas.
  * `-l LATENCY, --latency LATENCY` : latence. Préciser "low", "high" ou un nombre de secondes (par défaut, "high")
  * `-b BLOCKSIZE, --blocksize BLOCKSIZE` : taille des blocs. Nombre de frames pour chaque étape du mixeur. 0 (par défaut) signifie que le programme choisit lui-même le nombre qui lui convient.
  * `-f FRAME_RATE, --frame-rate FRAME_RATE` : fréquence d'échantillonnage pour jouer les musiques. Par défaut : 44100
  * `-x CHANNELS, --channels CHANNELS` : nombre de canaux par musique (2 par défaut, pour une écoute stéréo)
  * `-s SAMPLE_WIDTH, --sample-width SAMPLE_WIDTH` : largeur d'échantillonnage (nombre d'octets pour chaque frame). Par défaut : 2.
  * `--device DEVICE` : sélectionne le périphérique de son.
  * `--list-devices` : Affiche la liste des périphériques de son disponibles.
  * `-- ARGS` : Arguments à passer à la librairie Kivy.

## Configurer les touches

**ATTENTION : le format du fichier de configuration est susceptible d'évoluer, sans garantie de rétrocompatibilité.**

Le fichier config.yml utilise la syntaxe yaml. Les catégories et sous-catégories sont gérées par l'indentation par des espaces (mais PAS par des tabulations !).
le `#` est un symbole de commentaire : tout ce qui suit ce symbole sur une ligne est ignoré. 

En cas d'erreur dans le fichier de configuration, un message d'erreur s'affiche dans le terminal. Selon la "gravité" de l'erreur, music_sampler se lance en ignorant les actions erronées (en colorant éventuellement la touche en noir), ou ne se lance pas du tout.

Le fichier contient plusieurs sections :

    :::yaml
    aliases:
      ...

    music_properties:
      ...

    key_properties:
      ...

    keys:
      ...


### `music_properties` : propriétés des musiques

Cette section sert à définir des propriétés globales des musiques.

#### Exemples

    :::yaml
      "music1.mp3":
        name: My favorite music
        gain: 1.4
La musique "music1.mp3" est désignée par le nom "My favorite music". Elle est chargée à 140% de son volume normal.

    :::yaml
      "music2.mp3":
        gain: 0.7

La musique "music2.mp3" est chargée à 70% de son volume normal.

#### Liste des options possibles
- `name: My music` La musique sera désignée  (dans les actions, dans le terminal) comme "My music" au lieu du chemin du fichier. Par exemple le cadre des actions affichera "starting « My music » at volume 100%". Attention, cela ne fait pas office d'alias dans le fichier de configuration (voir la section *aliases*). 
- `gain: x` Charge la musique avec un gain de x (multiplicatif). Utiliser la commande "volume" pour changer ponctuellement le volume (0 à 100%) au cours de l'écoute.

### `key_properties` : affichage et propriétés des touches

Cette section sert à décrire l'affichage à l'écran des touches : couleur et texte. Par défaut, une touche "attribuée" à une ou plusieurs actions s'affiche en vert.

#### Exemples

    :::yaml
      'ESC':
        description:
          - 
          - STOP !
        color: [255, 0, 0]
        repeat_delay: 2

La touche échap est de couleur rouge, et le texte "STOP !" est affiché sur la deuxième ligne. Si on appuie deux fois sur la même touche à moins de deux secondes d'intervalle, le second appui est ignoré.

#### Liste des options possibles
- `description` : le texte qui s'affiche, à côté du "nom" de la touche. Il faut mettre un tiret pour une ligne de texte (pas de retour à la ligne automatique). La première ligne correspond à celle de la lettre associée à la touche, aussi il vaut mieux souvent la laisser vide, ou ne mettre que très peu de texte (voir l'exemple ci-dessus). Sur un écran de taille raisonnable, on peut compter 3 lignes (incluant la première) pour une touche "standard".
- `color: [r, g, b]` : la couleur de la touche. r, g et b sont les proportions de rouge, vert et bleu, et doivent être des entiers entre 0 et 255.
- `repeat_delay: x` (par défaut : 0) : délai de "sécurité" en cas d'appuis successifs sur la touche. La touche est désactivée (grisée et barrée) pendant toute la durée des actions puis le délai de x secondes.

### `keys` : actions sur les touches

Cette section sert à décrire, pour chaque touche, la liste des actions successives. Notez que la plupart des actions (hors `wait` et quelques cas particuliers, voir plus bas) sont quasi-instantanées.


#### Exemples

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

Lance la musique "music1.mp3" à 70% de son volume max, à 10 secondes du début, puis au bout de 5 secondes coupe la musique avec un fondu de 2 secondes.

    :::yaml
    'b':
      - stop: 
          file: "music1.mp3"
          fade_out: 5
          wait: false
      - play:
          file: "music2.mp3"
          fade_in: 5

Effectue un fondu enchaîné de 5 secondes entre "music1.mp3" et "music2.mp3"

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
Coupe la musique "music1.mp3" avec un fondu de 5 secondes, attend la fin du fondu, puis attend encore deux secondes et lance la musique "music2.mp3", au temps d'une minute.

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

Baisse le volume de "music1.mp3" pendant que le son "noise.mp3" est joué par dessus (deux fois). Le volume revient à la normale une fois que les deux écoutes du son "noise" sont terminées.

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

Met en pause la musique "music1.mp3" pour 10 secondes et la relance après, en avançant de 5 secondes dans la musique.

#### Liste des actions possibles: 
- `play` : joue une musique. music_sampler ne joue qu'une musique à la fois : si la musique demandée est déjà en train d'être jouée, elle n'est pas relancée ou jouée "par dessus". Paramètres :
    * `file: "music.mp3"` précise la musique jouée (chemin relatif).
    * `fade_in: x` (facultatif) lance la musique avec un fondu au départ de x secondes.
    * `volume: x` (facultatif, défaut : 100) la musique doit être jouée à x% de son volume max.
    * `loop: x` (facultatif, défaut : 0) la musique doit être répétée x fois. Indiquer -1 pour la répéter indéfiniment. Attention, x est le nombre de répétitions, donc pour lire trois fois la musique, mettre `loop: 2`.
    * `start_at: x` (facultatif, défaut : 0) la musique démarre à x secondes du début.
    * `restart_if_running: true/false` (facultatif, défaut : false) la musique est éventuellement stoppée et redémarrée si nécessaire
- `stop` : arrête une musique donnée. Paramètres :
    * `file: "music.mp3"` (facultatif) précise la musique à stopper. Si aucune musique n'est précisée, le `stop` s'applique à toutes les musiques.
    * `fade_out: x` (facultatif) stoppe la musique avec un fondu de x secondes.
    * `wait: true/false` (facultatif, par défaut : false) dans le cas d'un fondu, attendre la durée du fondu pour faire les actions suivantes. Si la musique s'arrêtait naturellement avant la fin du fondu, l'attente se termine lorsque la musique se termine naturellement. Lorsque plusieurs musiques sont stoppées en fondu, le `wait` n'attend que la dernière musique de la playlist (qui peut se terminer naturellement avant les autres).
    * `set_wait_id: name` (facultatif, inutile lorsque `wait` est à false) donne l'identifiant `name` à l'attente de fin du fondu (voir `interrupt_wait`). L'identifiant peut être n'importe quelle chaîne de caractère.
- `volume` : change le volume d'une musique donnée. Paramètres :
    * `file: "music.mp3"` (facultatif) précise la musique. Si aucune musique n'est précisée, la modification s'applique au volume global.
    * `delta: true/false` (facultatif, par défaut : false) le volume doit il être précisé en absolu (false), ou en relatif (true), voir plus bas.
    * `value: x` Si delta est à false, met le volume à x% du volume max (x doit être entre 0 et 100).
Ce facteur est appliqué à la musique déjà chargée en mémoire (voir section "propriétés"), donc le 100% fait référence au volume de chargement.
Si delta est à true, applique un modificateur de x% au volume (x doit être un entier signé).
Notez qu'une action "+10%" relative ne correspond pas à un pourcentage du volume actuel, mais du volume "de référence" 100%. Ainsi, effectuer +10% et -10% en relatif revient bien à 100%.
    * `fade: x` (facultatif) le changement de volume est appliqué en fondu sur x secondes. Il n'y a pas d'attente de la fin du fondu pour lancer les actions suivantes : au besoin, rajouter un `wait` à la main.
- `pause` : met en pause une musique. Paramètres :
    * `file: "music.mp3"` (facultatif) précise la musique à mettre en pause. Si non précisé, s'applique à toutes les musiques.
- `unpause` : relance une musique mise en pause (là où elle en était). Paramètres :
    * `file: "music.mp3"` (facultatif) précise la musique à relancer. Si non précisé, s'applique à toutes les musiques.
- `wait` : attend un temps donné. Paramètres :
    * `file: "music.mp3"` (facultatif) attend la fin de la musique "music.mp3"
    * `duration: x` (facultatif) attend x secondes. Si `file` et `duration` sont précisés, l'attente dure jusqu'à la fin de la musique PUIS la durée donnée par `duration`.
    * `set_wait_id: name` (facultatif) donne l'identifiant `name` à l'attente (voir `interrupt_wait`). L'identifiant peut être n'importe quelle chaîne de caractère.
Notez une fois encore que `wait` est quasiment la seule action qui attend d'avoir terminé pour lancer la commande suivante, toutes les autres sont lancées successivement mais sans attendre (donc presque simultanément) : ne pas hésiter à rajouter des commandes d'attente partout où c'est nécessaire.
- `seek` : permet d'aller à un endroit précis dans une musique. Paramètres :
    * `file: "music.mp3"` (facultatif) précise la musique. Si aucune musique n'est précisée, l'action s'applique à toutes les musiques.
    * `delta: true/false` (facultatif, défaut : false) Si `delta` est true, le temps est relatif. Si delta est false, le temps est absolu, voir plus bas.
    * `value: x` Si `delta` est true, alors fait avancer de x secondes dans la musique (reculer si x est négatif). Si delta est false, alors la lecture se place à x secondes à partir du début. Si la musique est en train de faire un fondu (au départ, ou changement de volume), le fondu se "termine automatiquement" : et la musique est immédiatement au volume final voulu. Si la musique est en train de se terminer en fondu, le "seek" est ignoré (un fondu de fin considère la musique comme déjà terminée). En cas de `loop`, si le déplacement est relatif la musique peut éventuellement passer à la répétition suivante / précédente; sinon, le déplacement se fait dans la répétition courante.
- `stop_all_actions:` Interrompt toutes les actions en cours et à faire. Notez qu'une musique lancée (y compris avec une option `loop`) est considérée comme une action "déjà terminée", et ne sera donc pas interrompue (utiliser `stop` sans arguments pour stopper toutes les musiques en écoute). Paramètre :
    * `other_only: true/false` (facultatif, défaut : false) : si `other_only` est true, la commande interrompt uniquement les actions des *autres* touches. Sinon, cette commande interrompt également les actions de la touche actuelle ; dans ce cas il est inutile de mettre des actions à la suite de celle-ci puisqu'elles seront systématiquement interrompues.
- `interrupt_wait`: interrompt l'attente (de `wait` ou fin d'un fondu avec attente) et passe directement à l'action suivante. Paramètre :
    * `wait_id: name` : précise l'identifiant du `wait` à stopper (défini par `set_wait_id`, voir les actions `wait` et `stop`). Pour interrompre plusieurs `wait` d'un seul coup, il faut mettre plusieurs `interrupt_wait`.
- `run_command` : lance une commande. Paramètres :
    * `command: my_command` : précise la commande à lancer.
    * `wait: true/false` (facultatif, défaut : false) : si `wait` est true, attend que la commande ait fini de s'exécuter.

### `aliases` : définir des alias

Il est possible de définir des alias pour les différents paramètres. Ces alias sont internes au fichier de configuration ; pour afficher un "joli" nom d'une musique, voir plutôt "music_properties".

La syntaxe est la suivante:

    :::yaml
    aliases:
      alias1:
        param: value
      alias2:
        param1: value1
        param2: value2

On utilise ensuite, dans le fichier de configuration, `include: alias1` ou `include: [alias1, alias2]` à la place de `param: value`. Dans le cas de plusieurs aliases inclus contenant des éléments identiques, seul le dernier est pris en compte. Dans tous les cas, les alias ne sont *pas* prioritaires par rapport aux éventuels paramètres définis là où ils sont inclus. Voir les exemples ci-dessous.

#### Exemples

    :::yaml
    aliases:
      music1:
        file: "path/to/my/favourite/music.mp3"

    keys:
      'a':
        play:
          include: music1

`music1` est désormais un alias pour `"path/to/my/favourite/music.mp3"`. À chaque fois qu'on veut écrire `file: "path/to/my/favourite/music.mp3"`, on peut écrire à la place `include: music1`. Attention, dans la section "music_properties", les alias ne fonctionnent pas, et il faut écrire le nom du fichier complet.

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

`blue` est un alias pour la couleur `[0, 0, 255]`. À chaque fois qu'on veut écrire `color: [0, 0, 255]`, on peut écrire `include: blue` à la place.

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

`long_time` est un alias pour la durée 42 secondes. Au lieu d'écrire `duration: 42`, on peut écrire `include: long_time`.

## Problèmes possibles

Sont listés ci-dessous une liste de problèmes rencontrés, avec des solutions proposées. Si vous en découvrez d'autre, contactez l'auteur pour les ajouter à la liste.

* Le programme se lance et s'arrête tout de suite.

Il s'agit généralement d'une erreur de syntaxe dans le fichier de config. Dans ce cas, le terminal doit afficher quelques détails sur l'erreur en question (au moins la ligne correspondante).

* La musique "grésille" affreusement.

Il peut s'agir d'un problème de latence (avec certains ordinateurs un peu lents). Essayez de changer la latence (par exemple, 0.1 seconde)

* Impossible de jouer plus d'une musique à la fois.

Le système n'arrive pas à mixer les musiques par lui-même. Vous pouvez essayer de regarder la liste des périphériques de son (`--list-devices`) puis en sélectionner un autre si disponible. Vous pouvez aussi essayer le mixeur intégré à music_sampler, mais les résultats ne sont pas toujours très fluides (ne pas hésiter à jouer avec les paramètres avancés comme latency et blocksize).

Si votre système utilise PulseAudio, il peut s'agir d'un problème de configuration du plugin ALSA. Dans ce cas, essayez de mettre la configuration suivante dans `/etc/asound.conf`, puis redémarrer la machine (solution empirique qui semble avoir fonctionné, sans garantie !):

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

* La console affiche une erreur :

        Exception in thread Thread-1:
        Traceback (most recent call last):
          File "threading.py", line 914, in _bootstrap_inner
          File "threading.py", line 862, in run
          File "kivy/input/providers/mtdev.py", line 219, in _thread_run
          File "kivy/lib/mtdev.py", line 131, in __init__
        PermissionError: [Errno 13] Permission denied: '/dev/input/event6'

C'est une erreur de permission d'accès à un périphérique, généré par la librairie kivy. Elle peut être ignorée et n'aura pas d'incidence.

* Pour d'autres problèmes ou bugs à reporter, voir le [Bug Tracker](https://git.immae.eu/mantisbt/view_all_bug_page.php?project_id=1&sort=status%2Clast_updated&dir=ASC%2CDESC)
## Divers

Les extraits de musiques proposés en exemples proviennent de [Jamendo](https://jamendo.com). Les musiques (complètes) sont disponibles en libre téléchargement pour un usage non commercial :

[Short Blues](https://www.jamendo.com/track/340173/short-blues)

[To the Fantasy war](https://www.jamendo.com/track/778560/to-the-fantasy-war)

Le bruit de crocodile provient de [Universal-Soundbank](http://www.universal-soundbank.com/).

Cet outil a été développé à l'origine pour faciliter la gestion du son pour les spectacles de la compagnie circassienne [Les pieds jaloux](http://piedsjaloux.fr/). N'ayant pas d'ingénieur son, les artistes eux-mêmes peuvent alors gérer leur musique lorsqu'ils ne sont pas sur scène : d'où la nécessité de préparer les transitions à l'avance et, au moment de la représentation, de réduire l'interaction avec la machine au minimum (une touche).

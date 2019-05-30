#import subprocess  # for running software outside of python
from subprocess import run
import requests  # high-level url interface
import urllib.request  # for accessing files from URLs


def setup_repositories():
    """Setup repositories for apps not in the default repos"""
    # TODO figure out how to use pipes to run.
    # wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
    # sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
    # sudo apt-get update  # run refresh after repo setup instead.
    print('setup_repositories not yet setup for automatic install')


def update():
    """Update then upgrade apt."""
    commands = ['update', 'upgrade']
    for command in commands:
        print('******'+command+'******')
        run(['sudo', 'apt', command])


def setup_swap():
    """Setup a swap file and ensure it is loaded with each restart."""
    print('******swap******')
    # Variables
    swap_size = '8G'
    swap_file = '/var/swap'
    permissions = '600'    # owner can read/write
    fstab_file = '/etc/fstab'

    # commands
    print('fallocate')
    # if swap_file does not exist then run the following
    try:
        # make the file
        run(['sudo', 'fallocate', '-l', swap_size, swap_file])

        # make the file a swap file
        print('mkswap')
        run(['sudo', 'mkswap', swap_file])

        # assign the swap file restricted permissions
        print('chmod')
        run(['sudo', 'chmod', permissions, swap_file])

        # turn the swap file on
        print('swapon')
        run(['sudo', 'swapon', swap_file])

        # update fstab to turn swap on after every reboot
        print('fstab')
        with open(fstab_file, 'a') as fstab:
            fstab.write('var/swap swap swap defaults 0 0')

        # show current swap status (for removing other swap files)
        print('swap status')
        run(['sudo', 'swapon', '--summary'])

    except:
        # else exit this function.
        raise
        return


def remove_apt():
    """Remove bloat applications."""
    print('******apt remove******')
    applications = ['ubuntu-web-launchers',  # Bloat amazon app.
                    'aisleriot',  # game
                    'gnome-mahjongg',  # game
                    'gnome-sudoku',  # game
                    'gnome-todo'  # default todo app
                    'remmina',  # remote desktop application.
                    'simple-scan',  # scanning app.
                    'rhythmbox',  # default music player.
                    'thunderbird',  # default email client.
                    'usb-creator-gtk',  # default usb creator.
                   ]
    for app in applications:
        print('******'+app+'******')
        run(['sudo', 'apt', 'remove', app])
    print('******autoremove******')
    run(['sudo', 'apt', 'autoremove'])


def install_apt():
    """Install applications that are available in default apt."""
    print('******apt install******')
    applications = ['git',  # Version control.
                    'geary',  # non-gmail email
                    'evolution',  # gmail email.
                    'quodlibet',  # Music player.
                    'gnome-tweaks',  # Finer grained destkop style editing.
                    'chrome-gnome-shell',  # App linking firefox with tweaks.
                    'syncthing',  # Point-to-point back-up manager.
                    # 'gnome-shell-timer',  # App for focussing productivity.
                    'transmission-gtk',  # Torrent downloader.
                    'texmaker',  # LaTeX editor (for editing resume).
                    'asunder',  # Music CD ripping.
                    'baobab',  # Disk usage analysis.
                    'nautilus-dropbox',  # Cloud storage client
                    'python3-pip',  # Python package manager
                    'pwgen',  # Generate secure passwords

                    'gnome-mines',  # Minesweeper game.
                    'gnome-calendar',  # calendar app.
                    # 'atom',  # requires custom atom repo
                   ]
    for app in applications:
        print('******'+app+'******')
        run(['sudo', 'apt', 'install', app])


def install_app_images():
    """Install all applications that are not available in apt by default."""

    # download_directory = '/home/tom/'
    file_extension = '.AppImage'

    # balenaEtcher (https://github.com/balena-io/etcher)
    print('******etcher******')
    # TODO compare versions before downloading.
    # Download the latest AppImage from github
    etcher_appname = 'etcher'
    etcher_url = 'https://github.com/balena-io/etcher/'
    releases_url = 'releases/latest/download/'
    reference_url = 'latest-linux.yml'
    request_url = etcher_url + releases_url + reference_url
    # download yml content and convert to a string
    yml = requests.get(request_url).content.decode()  
    for line in yml.split('\n'):
        if line[4:8] == 'url:':
            appimage_url = line[9:]
    request_url = etcher_url + releases_url + appimage_url
    output_file = etcher_appname + file_extension
    run(['wget', '-q', '--show-progress',
                    request_url,
                    '-O', output_file])
    #run(['sudo', 'chmod', '+x', output_file])


def install_flatpak():
    # TODO
    print('flatpak auto-install not yet implemented.')
    # https://flatpak.org/setup/Ubuntu/


def install_snap():
    """Install all applications that are best installed as a snap."""
    print('******snap******')
    applications_classic = ['skype',  # App for mentor calls.
                           ]
    applications = ['gitkraken',  # App for pretty git commands.
                   ]
    for app in applications_classic:
        print('******'+app+'******')
        run(['sudo', 'snap', 'install', app, '--classic'])
    for app in applications:
        print('******'+app+'******')
        run(['sudo', 'snap', 'install', app])


if __name__ == '__main__':
    setup_repositories()
    update()
    # setup_swap()  # Not needed as using a lvm swap partition now
    install_apt()
    remove_apt()
    install_app_images()
    # install_flatpak()  # not yet implemented
    install_snap()

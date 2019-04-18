import subprocess

def update():
    print('******update******')
    subprocess.run(['sudo', 'apt', 'update'])
    print('******')
    # print(subprocess.CompletedProcess)
    subprocess.run(['sudo', 'apt', 'upgrade'])

def setup_swap():
    print('******swap******')
    # Variables
    swap_size = '8G'
    swap_file = '/var/swap'
    permissions = '600'    # owner can read/write
    fstab_file = '/etc/fstab'



    # TODO check if the file exists

    # commands
    print('fallocate')
    # if swap_file does not exist then run the following
    try:
        # make the file
        subprocess.run(['sudo', 'fallocate', '-l', swap_size, swap_file])

        # make the file a swap file
        print('mkswap')
        subprocess.run(['sudo', 'mkswap', swap_file])

        # assign the swap file restricted permissions
        print('chmod')
        subprocess.run(['sudo', 'chmod', permissions, swap_file])

        # turn the swap file on
        print('swapon')
        subprocess.run(['sudo', 'swapon', swap_file])

        # update fstab to turn swap on after every reboot
        print('fstab')
        with open(fstab_file, 'a') as fstab:
            fstab.write('var/swap swap swap defaults 0 0')

        # show current swap status (for removing other swap files)
        print('swap status')
        subprocess.run(['sudo', 'swapon', '--summary'])

    except:
        # else exit this function.
        raise
        return


def install_apt_applications():
    """Install applications that are available in default apt."""
    print('******install******')
    applications = ['git',  # App for version control.
                    'geary',  # App for non-gmail email
                    'evolution',  # App for gmail email.
                    'quodlibet',  # App for music.
                    'gnome-tweaks',  # App for finer grained desktop style.
                    'chrome-gnome-shell',  # App linking firefox with tweaks.
                    'syncthing',  # App for managing back-ups and syncing.
                   ]
    for app in applications:
        print('******'+app+'******')
        subprocess.run(['sudo', 'apt', 'install', app])


def install_non_apt_applications():
    """Install all applications that are not available in apt by default."""

    # balenaEtcher (https://github.com/balena-io/etcher)
    print('******baleneEtcher******')
    # Add Etcher debian repository:
    balena_etcher_source_file = '/etc/apt/sources.list.d/balena-etcher.list'        
    with open(balena_etcher_source_file, 'w') as balena_etcher_source:
        balena_etcher_source.write("deb https://deb.etcher.io stable etcher")

    # Trust Bintray.com's GPG key:    
    subprocess.run(['sudo', 'apt-key', 'adv',
                    '--keyserver', 'keyserver.ubuntu.com',
                    '--recv-keys', '379CE192D401AB61'])

    # Update and install
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'balena-etcher-electron'])

update()
setup_swap()
install_apt_applications()
install_non_apt_applications()


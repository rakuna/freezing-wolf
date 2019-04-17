import subprocess

def update():
    print('******update******')
    subprocess.run(['apt', 'update'])
    print('******')
    print(subprocess.CompletedProcess)
    subprocess.run(['apt', 'upgrade'])

def setup_swap():
    print('******swap******')
    # Variables
    swap_size = '8G'
    swap_file = '/var/swap'
    permissions = '600'    # owner can read/write
    fstab_file = '/etc/fstab'

    # TODO
    # if swap_file does not exist then run the following
    # else exit this function.

    # commands
    # make the file
    print('fallocate')
    subprocess.run(['fallocate', '-l', swap_size, swap_file])

    # make the file a swap file
    print('mkswap')
    subprocess.run(['mkswap', swap_file])

    # assign the swap file restricted permissions
    print('chmod')
    subprocess.run(['chmod', permissions, swap_file])

    # turn the swap file on
    print('swapon')
    subprocess.run(['swapon', swap_file])

    # update fstab to turn swap on after every reboot
    print('fstab')
    with open(fstab_file, 'a') as fstab:
        fstab.write('var/swap swap swap defaults 0 0')

    # show current swap status (for removing other swap files)
    print('swap status')
    subprocess.run(['swapon', '--summary'])

def install_applications():
    print('******install******')
    applications = ['git']
    for app in applications:
        print('******'+app+'******')
        subprocess.run(['apt', 'install', app])

update()
setup_swap()
install_applications()

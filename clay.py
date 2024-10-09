import subprocess
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def aktifinterfacebulma():
    result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    output = result.stdout
    
    for line in output.splitlines():
        if "Connected" in line and "Dedicated" in line:
            interface_name = " ".join(line.split()[3:])
            print(f"Detected Interface Name: {interface_name}")
            return interface_name

    raise Exception("No active network interface found")

def dnsdegistirme(interface, dns1, dns2):
    print(f"Using interface: {interface}")
    subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', f'name={interface}', 'static', dns1], check=True)
    subprocess.run(['netsh', 'interface', 'ip', 'add', 'dns', f'name={interface}', dns2, 'index=2'], check=True)

banner = r"""
                                  ...
               s,                .                    .s
                ss,              . ..               .ss
                'SsSs,           ..  .           .sSsS'
                 sSs'sSs,        .   .        .sSs'sSs
                  sSs  'sSs,      ...      .sSs'  sSs
                   sS,    'sSs,         .sSs'    .Ss
                   'Ss       'sSs,   .sSs'       sS'
          ...       sSs  CLAY   ' .sSs'   CLAY  sSs       ...
         .           sSs       .sSs' ..,       sSs       .
         . ..         sS,   .sSs'  .  'sSs,   .Ss        . ..
         ..  .        'Ss .Ss'     .     'sSs. ''        ..  .
         .   .         sSs '       .        'sSs,        .   .
          ...      .sS.'sSs        .        .. 'sSs,      ...
                .sSs'    sS,     .....     .Ss    'sSs,
             .sSs'       'Ss       .       sS'       'sSs,
          .sSs'   CLAY    sSs      .      sSs   CLAY    'sSs,
       .sSs'____________________________ sSs ______________'sSs,
    .sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,
                            ...         sS'
                             sSs   C   sSs
                              sSs  L  sSs   
                               sS, A .Ss
                               'Ss Y sS'
                                sSs sSs
                                 sSsSs
                                  sSs
                                   s

                             PLEASE ENTER!
"""

System.Clear()
System.Title("C17K(clay) Discord No Vpn")
System.Size(75, 35)

Anime.Fade(Center.Center(banner), Colors.red_to_black, Colorate.Vertical, enter=True)

interface = aktifinterfacebulma()

dns1 = "8.8.8.8"
dns2 = "8.8.4.4"

dnsdegistirme(interface, dns1, dns2)

print(f"DNS settings for {interface} have been updated to {dns1} and {dns2}")

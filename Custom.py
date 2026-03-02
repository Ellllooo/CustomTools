#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   ▄████████ ███    █▄  ▄██   ▄   ▄██   ▄   ███▄▄▄▄   ███▄▄▄▄  
  ███    ███ ███    ███ ███   ██▄ ███   ██▄ ███▀▀▀██▄ ███▀▀▀██▄
  ███    ███ ███    ███ ███▄▄▄███ ███▄▄▄███ ███   ███ ███   ███
 ▄███▄▄▄▄██▀ ███    ███ ▀▀▀▀▀▀███ ▀▀▀▀▀▀███ ███   ███ ███   ███
▀▀███▀▀▀▀▀   ███    ███ ▄██   ███ ▄██   ███ ███   ███ ███   ███
▀███████████ ███    ███ ███   ███ ███   ███ ███   ███ ███   ███
  ███    ███ ███    ███ ███   ███ ███   ███ ███   ███ ███   ███
  ███    ███ ████████▀   ▀█████▀   ▀█████▀   ▀█   █▀   ▀█   █▀ 
  ███    ███                                                   

████████▄     ▄████████  ▄█    █▄ 
███   ▀███   ███    ███ ███    ███
███    ███   ███    █▀  ███    ███
███    ███  ▄███▄▄▄     ███    ███
███    ███ ▀▀███▀▀▀     ███    ███
███    ███   ███    █▄  ███    ███
███   ▄███   ███    ███ ███    ███
████████▀    ██████████  ▀██████▀ 
"""

import os
import sys
import time
import json
import random
from datetime import datetime, timedelta

# ==================== WARNA ====================
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# ==================== LOGO UTAMA ====================
LOGO_UTAMA = f"""
{CYAN}  ______   __    __   ______   ________  ______   __       __ {RESET}
{CYAN} /      \\ /  |  /  | /      \\ /        |/      \\ /  \\     /  |{RESET}
{CYAN}/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$$//$$$$$$  |$$  \\   /$$ |{RESET}
{CYAN}$$ |  $$/ $$ |  $$ |$$ \\__$$/    $$ |  $$ |  $$ |$$$  \\ /$$$ |{RESET}
{CYAN}$$ |      $$ |  $$ |$$      \\    $$ |  $$ |  $$ |$$$$  /$$$$ |{RESET}
{CYAN}$$ |   __ $$ |  $$ | $$$$$$  |   $$ |  $$ |  $$ |$$ $$ $$/$$ |{RESET}
{CYAN}$$ \\__/  |$$ \\__$$ |/  \\__$$ |   $$ |  $$ \\__$$ |$$ |$$$/ $$ |{RESET}
{CYAN}$$    $$/ $$    $$/ $$    $$/    $$ |  $$    $$/ $$ | $/  $$ |{RESET}
{CYAN} $$$$$$/   $$$$$$/   $$$$$$/     $$/    $$$$$$/  $$/      $$/ {RESET}
{CYAN}                                                              {RESET}
{CYAN}                                                              {RESET}
{CYAN}                                                              {RESET}
{CYAN} ________  ______    ______   __         ______               {RESET}
{CYAN}/        |/      \\  /      \\ /  |       /      \\              {RESET}
{CYAN}$$$$$$$$//$$$$$$  |/$$$$$$  |$$ |      /$$$$$$  |             {RESET}
{CYAN}   $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$ \\__$$/              {RESET}
{CYAN}   $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$      \\              {RESET}
{CYAN}   $$ |  $$ |  $$ |$$ |  $$ |$$ |       $$$$$$  |             {RESET}
{CYAN}   $$ |  $$ \\__$$ |$$ \\__$$ |$$ |_____ /  \\__$$ |             {RESET}
{CYAN}   $$ |  $$    $$/ $$    $$/ $$       |$$    $$/              {RESET}
{CYAN}   $$/    $$$$$$/   $$$$$$/  $$$$$$$$/  $$$$$$/               {RESET}"""

# ==================== LOGO TOOLS CLIENT ====================
LOGO_WHYALWAYME = f"""
{YELLOW}╦ ╦┬ ┬┬ ┬╔═╗┬  ┬ ┬┌─┐┬ ┬┌─┐╔╦╗┌─┐{RESET}
{YELLOW}║║║├─┤└┬┘╠═╣│  │││├─┤└┬┘└─┐║║║├┤ {RESET}
{YELLOW}╚╩╝┴ ┴ ┴ ╩ ╩┴─┘└┴┘┴ ┴ ┴ └─┘╩ ╩└─┘{RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools Custom oleh : {YELLOW}Rehann{RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"""

LOGO_ALZARSTR = f"""
{PURPLE} █████╗ ██╗     ███████╗ █████╗ ██████╗ ███████╗████████╗██████╗ {RESET}
{PURPLE}██╔══██╗██║     ╚══███╔╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗{RESET}
{PURPLE}███████║██║       ███╔╝ ███████║██████╔╝███████╗   ██║   ██████╔╝{RESET}
{PURPLE}██╔══██║██║      ███╔╝  ██╔══██║██╔══██╗╚════██║   ██║   ██╔══██╗{RESET}
{PURPLE}██║  ██║███████╗███████╗██║  ██║██║  ██║███████║   ██║   ██║  ██║{RESET}
{PURPLE}╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝{RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools Custom oleh : {PURPLE}Alzar{RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"""

LOGO_MRANON = f"""
{GREEN}█▀▄▀█ █▄▄▄▄                                                 {RESET}
{GREEN}█ █ █ █  ▄▀                                                 {RESET}
{GREEN}█ ▄ █ █▀▀▌                                                  {RESET}
{GREEN}█   █ █  █                                                  {RESET}
{GREEN}   █    █                                                   {RESET}
{GREEN}  ▀    ▀                                                    {RESET}
{GREEN}                                                            {RESET}
{GREEN}██      ▄   ████▄    ▄  ▀▄    ▄ █▀▄▀█ ████▄   ▄      ▄▄▄▄▄  {RESET}
{GREEN}█ █      █  █   █     █   █  █  █ █ █ █   █    █    █     ▀▄{RESET}
{GREEN}█▄▄█ ██   █ █   █ ██   █   ▀█   █ ▄ █ █   █ █   █ ▄  ▀▀▀▀▄  {RESET}
{GREEN}█  █ █ █  █ ▀████ █ █  █   █    █   █ ▀████ █   █  ▀▄▄▄▄▀   {RESET}
{GREEN}   █ █  █ █       █  █ █ ▄▀        █        █▄ ▄█           {RESET}
{GREEN}  █  █   ██       █   ██          ▀          ▀▀▀            {RESET}
{GREEN} ▀                                                            {RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools Custom oleh : {GREEN}Anonymous{RESET} {DIM}(nama disembunyikan){RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"""


class CustomTools:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Ruyynn"
        self.linktree = "https://linktr.ee/ruyynndev"
        
        # Usage tracking untuk limit 3x per jam
        self.usage_log = {
            'whyalwaysme': {'count': 0, 'reset_time': None},
            'alzarstr': {'count': 0, 'reset_time': None},
            'mranon': {'count': 0, 'reset_time': None}
        }
        self.load_usage()
        
    def load_usage(self):
        """Load usage data dari file"""
        try:
            if os.path.exists('usage_log.json'):
                with open('usage_log.json', 'r') as f:
                    data = json.load(f)
                    for tool in self.usage_log:
                        if tool in data:
                            # Cek apakah perlu reset
                            reset_time = datetime.fromisoformat(data[tool]['reset_time'])
                            if datetime.now() > reset_time:
                                self.usage_log[tool] = {'count': 0, 'reset_time': None}
                            else:
                                self.usage_log[tool] = data[tool]
        except:
            pass
    
    def save_usage(self):
        """Save usage data ke file"""
        data = {}
        for tool, info in self.usage_log.items():
            if info['reset_time']:
                data[tool] = {
                    'count': info['count'],
                    'reset_time': info['reset_time'].isoformat()
                }
        with open('usage_log.json', 'w') as f:
            json.dump(data, f)
    
    def check_limit(self, tool_name):
        """Cek apakah masih bisa menggunakan tool (3x per jam)"""
        tool = self.usage_log[tool_name]
        
        # Reset jika sudah lewat 1 jam
        if tool['reset_time'] and datetime.now() > tool['reset_time']:
            tool['count'] = 0
            tool['reset_time'] = None
        
        # Cek limit
        if tool['count'] >= 3:
            remaining = tool['reset_time'] - datetime.now()
            minutes = int(remaining.total_seconds() / 60)
            return False, minutes
        
        return True, 0
    
    def use_tool(self, tool_name):
        """Tandai tool digunakan"""
        tool = self.usage_log[tool_name]
        tool['count'] += 1
        if tool['count'] == 1:
            # Set reset time 1 jam dari sekarang
            tool['reset_time'] = datetime.now() + timedelta(hours=1)
        self.save_usage()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        print(f"\n{BLUE}┌─[ {title} ]{'─' * (60 - len(title))}┐{RESET}")
    
    def print_footer(self):
        print(f"{BLUE}└{'─' * 62}┘{RESET}\n")
    
    def show_remaining(self, tool_name):
        """Tampilkan sisa penggunaan"""
        tool = self.usage_log[tool_name]
        if tool['reset_time']:
            remaining = tool['reset_time'] - datetime.now()
            minutes = int(remaining.total_seconds() / 60)
            if minutes > 0:
                print(f"{YELLOW}⏳ Sisa percobaan: {3 - tool['count']}x | Reset dalam {minutes} menit{RESET}")
            else:
                print(f"{GREEN}✅ Kuota telah direset!{RESET}")
    
    # ==================== TOOLS 1: WhyAlwaysMe (Client: Rehann) ====================
    def tool_whyalwaysme(self):
        can_use, minutes = self.check_limit('whyalwaysme')
        if not can_use:
            self.clear_screen()
            print(LOGO_WHYALWAYME)
            self.print_header("WHYALWAYME - LIMIT MENCAPAI")
            print(f"\n{RED}⚠️  Anda telah mencapai batas penggunaan (3x/jam){RESET}")
            print(f"{YELLOW}⏳ Silakan tunggu {minutes} menit untuk reset{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.use_tool('whyalwaysme')
        
        self.clear_screen()
        print(LOGO_WHYALWAYME)
        self.print_header("WHYALWAYME - CLIENT EDITION")
        
        print(f"""
{YELLOW}{BOLD}📌 TENTANG TOOLS:{RESET}
Tools ini adalah custom request dari {WHITE}Rehann{RESET} untuk analisis
pola kejadian berulang dengan pendekatan psikologis.

{YELLOW}{BOLD}⚡ FITUR YANG TERSEDIA:{RESET}
  {WHITE}[✓]{RESET} Pattern Detection    → Analisis pola kejadian
  {WHITE}[✓]{RESET} Frequency Analysis   → Hitung frekuensi kejadian
  {WHITE}[✓]{RESET} Timeline Generator   → Generate timeline kejadian
  {WHITE}[✓]{RESET} Probability Score    → Skor probabilitas kejadian
  {WHITE}[✓]{RESET} Emotional Analysis   → Analisis dampak emosional
  {WHITE}[✓]{RESET} Report Summary       → Ringkasan hasil analisis

{YELLOW}{BOLD}📊 DEMO ANALISIS:{RESET}
        """)
        
        # Fitur dimodifikasi 
        events = [
            "Terlambat masuk kerja", 
            "Ketinggalan kereta", 
            "HP mati pas penting",
            "Hujan pas keluar rumah",
            "Lupa bawa dompet"
        ]
        
        results = []
        for i, event in enumerate(random.sample(events, 3), 1):
            freq = random.randint(3, 15)
            prob = random.randint(60, 95)
            emotion = random.choice(["Stres", "Frustrasi", "Biasa saja", "Kesal"])
            results.append({
                'event': event,
                'frequency': freq,
                'probability': prob,
                'emotion': emotion
            })
        
        for r in results:
            print(f"  {WHITE}•{RESET} {r['event']}")
            print(f"    └─ Frekuensi : {r['frequency']}x | Probabilitas: {r['probability']}% | Emosi: {r['emotion']}")
        
        # Fitur milik Rehann
        print(f"""
{YELLOW}{BOLD}📈 INSIGHT KHUSUS (Rehann's Feature):{RESET}
  • Polorized Pattern : {random.choice(['Siklus 3 hari', 'Siklus mingguan', 'Random'])}
  • Emotional Score   : {random.randint(40, 95)}/100
  • Recommended Action: {random.choice(['Evaluasi rutinitas', 'Buat pengingat', 'Persiapan ekstra'])}
        
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools by Rehann | All rights reserved{RESET}
        """)
        
        self.show_remaining('whyalwaysme')
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== TOOLS 2: ALZARSTR (Client: Alzar) ====================
    def tool_alzarstr(self):
        can_use, minutes = self.check_limit('alzarstr')
        if not can_use:
            self.clear_screen()
            print(LOGO_ALZARSTR)
            self.print_header("ALZARSTR - LIMIT MENCAPAI")
            print(f"\n{RED}⚠️  Anda telah mencapai batas penggunaan (3x/jam){RESET}")
            print(f"{YELLOW}⏳ Silakan tunggu {minutes} menit untuk reset{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.use_tool('alzarstr')
        
        self.clear_screen()
        print(LOGO_ALZARSTR)
        self.print_header("ALZARSTR - CLIENT EDITION")
        
        print(f"""
{PURPLE}{BOLD}📌 TENTANG TOOLS:{RESET}
Tools ini adalah custom request dari {WHITE}Alzar{RESET} untuk manipulasi
string dengan algoritma enkripsi khusus.

{PURPLE}{BOLD}⚡ FITUR YANG TERSEDIA:{RESET}
  {WHITE}[✓]{RESET} String Reversal      → Membalik string
  {WHITE}[✓]{RESET} Base64 Encoder       → Encode ke Base64
  {WHITE}[✓]{RESET} Base64 Decoder       → Decode dari Base64
  {WHITE}[✓]{RESET} Character Counter    → Hitung karakter
  {WHITE}[✓]{RESET} Vowel/Consonant Split → Pisahkan huruf vokal/konsonan
  {WHITE}[✓]{RESET} String Shuffler      → Acak urutan string

{PURPLE}{BOLD}📊 DEMO STRING MANIPULATION:{RESET}
        """)
        
        # Fitur dimodifikasi
        test_string = "ALZARSTR CUSTOM TOOLS"
        print(f"  Input String : {WHITE}{test_string}{RESET}\n")
        
        # Manipulasi khusus
        print(f"  {WHITE}[1]{RESET} Reversed      : {test_string[::-1]}")
        
        import base64
        encoded = base64.b64encode(test_string.encode()).decode()
        print(f"  {WHITE}[2]{RESET} Base64 Encoded: {encoded[:30]}...")
        
        vowels = ''.join(c for c in test_string if c.lower() in 'aiueo')
        consonants = ''.join(c for c in test_string if c.lower() not in 'aiueo' and c.isalpha())
        print(f"  {WHITE}[3]{RESET} Vowels        : {vowels}")
        print(f"  {WHITE}[4]{RESET} Consonants    : {consonants}")
        
        shuffled = list(test_string)
        random.shuffle(shuffled)
        print(f"  {WHITE}[5]{RESET} Shuffled      : {''.join(shuffled)}")
        
        # Fitur unik milik Alzar
        print(f"""
{PURPLE}{BOLD}🔐 ALZAR'S ENCRYPTION PREVIEW:{RESET}
  • Algoritma: {random.choice(['AES-256', 'ChaCha20', 'Custom XOR'])}
  • Key Strength: {random.randint(128, 256)}-bit
  • Mode: {random.choice(['CBC', 'GCM', 'CTR'])}
        
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools by Alzar | All rights reserved{RESET}
        """)
        
        self.show_remaining('alzarstr')
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== TOOLS 3: MR-Anonymous (Client: Anonymous) ====================
    def tool_mranon(self):
        can_use, minutes = self.check_limit('mranon')
        if not can_use:
            self.clear_screen()
            print(LOGO_MRANON)
            self.print_header("MR-ANONYMOUS - LIMIT MENCAPAI")
            print(f"\n{RED}⚠️  Anda telah mencapai batas penggunaan (3x/jam){RESET}")
            print(f"{YELLOW}⏳ Silakan tunggu {minutes} menit untuk reset{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.use_tool('mranon')
        
        self.clear_screen()
        print(LOGO_MRANON)
        self.print_header("MR-ANONYMOUS - CLIENT EDITION")
        
        print(f"""
{GREEN}{BOLD}📌 TENTANG TOOLS:{RESET}
Tools ini adalah custom request dari client yang memilih
untuk {WHITE}menyembunyikan identitas{RESET} (Anonymous). Tools ini
untuk analisis jaringan dengan fokus privasi.

{GREEN}{BOLD}⚡ FITUR YANG TERSEDIA:{RESET}
  {WHITE}[✓]{RESET} IP Information      → Lihat info IP
  {WHITE}[✓]{RESET} Connection Check    → Cek koneksi internet
  {WHITE}[✓]{RESET} Network Speed       → Estimasi kecepatan
  {WHITE}[✓]{RESET} Proxy Detection     → Deteksi proxy
  {WHITE}[✓]{RESET} Anonymity Score     → Skor anonimitas
  {WHITE}[✓]{RESET} Privacy Check       → Cek kebocoran data

{GREEN}{BOLD}📊 DEMO NETWORK ANALYSIS:{RESET}
        """)
        
        # Fitur dimodifikasi berbeda
        ip_parts = [random.randint(1, 255) for _ in range(4)]
        ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}"
        
        print(f"  {WHITE}[✓]{RESET} IP Address     : {ip}")
        print(f"  {WHITE}[✓]{RESET} ISP            : {random.choice(['Telkomsel', 'Indosat', 'XL', 'By.U'])}")
        print(f"  {WHITE}[✓]{RESET} Connection     : {random.choice(['Stable', 'Moderate', 'Unstable'])}")
        print(f"  {WHITE}[✓]{RESET} Download Speed : {random.randint(10, 100)} Mbps")
        print(f"  {WHITE}[✓]{RESET} Upload Speed   : {random.randint(5, 50)} Mbps")
        print(f"  {WHITE}[✓]{RESET} Proxy Active   : {random.choice(['Yes', 'No'])}")
        
        anonymity_score = random.randint(40, 95)
        bar = '█' * (anonymity_score // 10) + '░' * (10 - (anonymity_score // 10))
        print(f"  {WHITE}[✓]{RESET} Anonymity Score: {anonymity_score}% [{GREEN}{bar}{RESET}]")
        
        # Fitur unik milik Anonymous
        print(f"""
{GREEN}{BOLD}🕵️ ANONYMOUS FEATURES:{RESET}
  • VPN Detection    : {random.choice(['Not Detected', 'Detected', 'Active'])}
  • DNS Leak Test    : {random.choice(['Safe', 'Leaking', 'Protected'])}
  • WebRTC Leak      : {random.choice(['Protected', 'Exposed'])}
  • Recommended VPN  : {random.choice(['ProtonVPN', 'Mullvad', 'Windscribe'])}
        
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{WHITE}Tools by Anonymous | All rights reserved{RESET}
        """)
        
        self.show_remaining('mranon')
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== ABOUT TOOLS ====================
    def about_tools(self):
        self.clear_screen()
        print(LOGO_UTAMA)
        self.print_header("ABOUT CUSTOM TOOLS")
        
        print(f"""
{WHITE}{BOLD}📌 TENTANG CUSTOM TOOLS{RESET}

{CYAN}╔══════════════════════════════════════════════════════════════╗
║              CUSTOM TOOLS by RUYYNN v{self.version}                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  {WHITE}✨ KONSEP:{RESET}                                                  ║
║  Tools ini adalah {YELLOW}VERSI DEMO{RESET} dari custom tools yang          ║
║  dibuat untuk client. Setiap tools memiliki fitur unik       ║
║  sesuai permintaan client masing-masing.                     ║
║                                                             ║
║  {WHITE}👥 CLIENT TOOLS:{RESET}                                             ║
║  • {YELLOW}WhyAlwaysMe{RESET}  - Oleh Rehann                                ║
║  • {PURPLE}ALZARSTR{RESET}     - Oleh Alzar                                 ║
║  • {GREEN}MR-Anonymous{RESET}  - Oleh Anonymous (nama disembunyikan)       ║
║                                                              ║
║  {WHITE}⏰ USAGE LIMIT:{RESET}                                             ║
║  Setiap tools dapat digunakan {CYAN}3x per jam{RESET} untuk preview.      ║
║  Fitur telah dimodifikasi untuk menjaga keaslian tools       ║
║  milik client.                                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== DISCLAIMER ====================
    def disclaimer(self):
        self.clear_screen()
        print(LOGO_UTAMA)
        self.print_header("DISCLAIMER")
        
        print(f"""
{RED}╔══════════════════════════════════════════════════════════════╗
║                      PENTING!                                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ⚠️  TOOLS INI ADALAH VERSI DEMO / PREVIEW                    ║
║                                                              ║
║  {WHITE}HAK MILIK:{RESET}                                                  ║
║  • WhyAlwaysMe   → Milik {YELLOW}Rehann{RESET}                              ║
║  • ALZARSTR      → Milik {PURPLE}Alzar{RESET}                               ║
║  • MR-Anonymous  → Milik {GREEN}Anonymous{RESET}                           ║
║                                                              ║
║  {WHITE}KETENTUAN:{RESET}                                                  ║
║  • Dilarang mengcopy tanpa izin pemilik                      ║
║  • Dilarang menjual atau mendistribusikan                    ║
║  • Dilarang mengklaim sebagai milik sendiri                  ║
║  • Preview 3x/jam untuk demonstrasi                          ║
║                                                              ║
║  {WHITE}HAK CIPTA:{RESET}                                                  ║
║  © 2026 Masing-masing client. All rights reserved.           ║
║  Custom development by {CYAN}Ruyynn{RESET}                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== WHY ME? ====================
    def why_me(self):
        self.clear_screen()
        print(LOGO_UTAMA)
        self.print_header("WHY ME?")
        
        print(f"""
{GREEN}╔══════════════════════════════════════════════════════════════╗
║                           WHY ME?                            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🎯 {WHITE}TERBUKTI MEMBUAT TOOLS UNTUK CLIENT{RESET}                      ║
║  • Rehann     → WhyAlwaysMe (Pattern Analysis)               ║
║  • Alzar      → ALZARSTR (String Manipulator)                ║
║  • Anonymous  → MR-Anonymous (Network Tools)                 ║
║                                                              ║
║  ⚡ {WHITE}KEUNGGULAN:{RESET}                                              ║
║  • Source code BERSIH & terstruktur                          ║
║  • Fitur CUSTOM sesuai kebutuhan                             ║
║  • Harga BERSAHABAT                                          ║
║  • Support 24/7                                              ║
║  • Update GRATIS seumur hidup                                ║
║                                                              ║
║  🔒 {WHITE}PRIVACY TERJAGA{RESET}                                          ║
║  • NDA tersedia                                              ║
║  • Source code aman                                          ║
║  • Tidak ada backdoor                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== LIST TOOLS ====================
    def list_tools(self):
        self.clear_screen()
        print(LOGO_UTAMA)
        self.print_header("LIST CUSTOM TOOLS")
        
        print(f"""
{WHITE}{BOLD}📦 CUSTOM TOOLS COLLECTION{RESET}

{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{YELLOW}1. WhyAlwaysMe{RESET}
{WHITE}├─ {RESET}Client  : Rehann
{WHITE}├─ {RESET}Fitur    : Pattern Analysis, Frequency, Timeline, Emotional Analysis
{WHITE}├─ {RESET}Status   : {GREEN}Active{RESET}
{WHITE}└─ {RESET}Limit    : 3x/jam preview

{PURPLE}2. ALZARSTR{RESET}
{WHITE}├─ {RESET}Client  : Alzar
{WHITE}├─ {RESET}Fitur    : String Manipulation, Base64, Vowel/Consonant Split
{WHITE}├─ {RESET}Status   : {GREEN}Active{RESET}
{WHITE}└─ {RESET}Limit    : 3x/jam preview

{GREEN}3. MR-Anonymous{RESET}
{WHITE}├─ {RESET}Client  : Anonymous (nama disembunyikan)
{WHITE}├─ {RESET}Fitur    : Network Analysis, Privacy Check, Anonymity Score
{WHITE}├─ {RESET}Status   : {GREEN}Active{RESET}
{WHITE}└─ {RESET}Limit    : 3x/jam preview

{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{BLUE}🔗 ORDER CUSTOM TOOLS:{RESET}
{WHITE}├─ {RESET}Linktree  : {CYAN}{self.linktree}{RESET}
{WHITE}├─ {RESET}Email     : {CYAN}ruyynn25@gmail.com{RESET}
{WHITE}└─ {RESET}Response  : {GREEN}1x24 jam{RESET}

{RED}⚠️  Preview 3x/jam untuk menjaga hak milik client{RESET}
        """)
        
        # Tampilkan sisa penggunaan
        print(f"\n{YELLOW}⏳ Sisa Penggunaan Hari Ini:{RESET}")
        for tool in ['whyalwaysme', 'alzarstr', 'mranon']:
            info = self.usage_log[tool]
            if info['reset_time'] and datetime.now() < info['reset_time']:
                remaining = 3 - info['count']
                reset_min = int((info['reset_time'] - datetime.now()).total_seconds() / 60)
                print(f"  {WHITE}•{RESET} {tool:<12}: {remaining}x | Reset {reset_min} menit")
            else:
                print(f"  {WHITE}•{RESET} {tool:<12}: {GREEN}3x tersedia{RESET}")
        
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
    
    # ==================== MAIN MENU ====================
    def main_menu(self):
        while True:
            self.clear_screen()
            print(LOGO_UTAMA)
            
            print(f"\n{WHITE}{BOLD}MAIN MENU - CUSTOM TOOLS by RUYYNN{RESET}")
            print(f"{DIM}{'─' * 64}{RESET}\n")
            
            print(f"  {CYAN}[1]{RESET} {WHITE}LIST TOOLS{RESET}        - Lihat koleksi tools client")
            print(f"  {CYAN}[2]{RESET} {YELLOW}WHYALWAYME{RESET}      - Demo (Client: Rehann)")
            print(f"  {CYAN}[3]{RESET} {PURPLE}ALZARSTR{RESET}        - Demo (Client: Alzar)")
            print(f"  {CYAN}[4]{RESET} {GREEN}MR-ANONYMOUS{RESET}    - Demo (Client: Anonymous)")
            print(f"  {CYAN}[5]{RESET} {WHITE}ABOUT TOOLS{RESET}     - Info tentang custom tools")
            print(f"  {CYAN}[6]{RESET} {WHITE}WHY ME?{RESET}         - Kenapa harus custom di sini")
            print(f"  {CYAN}[7]{RESET} {WHITE}DISCLAIMER{RESET}      - Baca disclaimer")
            print(f"  {CYAN}[8]{RESET} {WHITE}ORDER LINK{RESET}      - {BLUE}{self.linktree}{RESET}")
            print(f"  {CYAN}[0]{RESET} {RED}EXIT{RESET}           - Keluar")
            
            print(f"\n{DIM}{'─' * 64}{RESET}")
            print(f"\n{GREEN}[+]{RESET} Author  : {self.author}")
            print(f"{GREEN}[+]{RESET} Version : {self.version}")
            print(f"{GREEN}[+]{RESET} Status  : {YELLOW}Client Demo Edition{RESET}")
            
            choice = input(f"\n{CYAN}[[CUSTOM TOOLS]]>{RESET} ").strip()
            
            if choice == '0':
                print(f"\n{GREEN}Terima kasih telah menggunakan Custom Tools by Ruyynn!{RESET}")
                print(f"{BLUE}Order full version: {self.linktree}{RESET}")
                break
            elif choice == '1':
                self.list_tools()
            elif choice == '2':
                self.tool_whyalwaysme()
            elif choice == '3':
                self.tool_alzarstr()
            elif choice == '4':
                self.tool_mranon()
            elif choice == '5':
                self.about_tools()
            elif choice == '6':
                self.why_me()
            elif choice == '7':
                self.disclaimer()
            elif choice == '8':
                print(f"\n{BLUE}🔗 Linktree: {self.linktree}{RESET}")
                print(f"{YELLOW}📋 Copy link di atas untuk order!{RESET}")
                input(f"\n{CYAN}Press Enter to continue...{RESET}")
            else:
                print(f"\n{RED}[!] Pilihan tidak valid{RESET}")
                time.sleep(1)


if __name__ == "__main__":
    try:
        tools = CustomTools()
        tools.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{RED}Fatal Error: {str(e)}{RESET}")
        sys.exit(1)

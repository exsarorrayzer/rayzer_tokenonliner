# CODDED BY RAYZER
import asyncio # By Rayzer
import websockets # By Rayzer
import json # By Rayzer
from rich.console import Console # By Rayzer
from rich.panel import Panel # By Rayzer

console = Console() # By Rayzer

banner_text = '''
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗            
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║            
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║            
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║            
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║            
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝            
                                                        
 ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗██████╗ 
██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝██╔══██╗
██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
''' # By Rayzer

console.print(Panel(banner_text, title="Token Online Tool | By Rayzer", style="bold magenta")) # By Rayzer
token = console.input("[bold cyan]Token gir: [/bold cyan]") # By Rayzer

GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json" # By Rayzer

async def keep_online(token): # By Rayzer
    headers = {"Authorization": token} # By Rayzer
    retry_count = 0 # By Rayzer
    while retry_count < 5: # By Rayzer
        try: # By Rayzer
            async with websockets.connect(GATEWAY_URL, extra_headers=headers) as ws: # By Rayzer
                console.print("[green]Bağlantı kuruldu, hesap online durumda. CTRL+C ile çıkabilirsin.[/green]") # By Rayzer
                hello = json.loads(await ws.recv()) # By Rayzer
                heartbeat_interval = hello['d']['heartbeat_interval'] / 1000 # By Rayzer

                async def send_heartbeat(): # By Rayzer
                    while True: # By Rayzer
                        await asyncio.sleep(heartbeat_interval) # By Rayzer
                        await ws.send(json.dumps({"op": 1, "d": None})) # By Rayzer

                asyncio.create_task(send_heartbeat()) # By Rayzer

                while True: # By Rayzer
                    await ws.recv() # By Rayzer

        except (websockets.exceptions.ConnectionClosedError, asyncio.TimeoutError): # By Rayzer
            console.print("[yellow]Bağlantı kapandı, yeniden bağlanıyor...[/yellow]") # By Rayzer
            retry_count += 1 # By Rayzer
            await asyncio.sleep(10) # By Rayzer

        except Exception as e: # By Rayzer
            console.print(f"[bold red]Beklenmedik hata:[/bold red] {e}") # By Rayzer
            break # By Rayzer

    console.print("[bold red]Çok fazla yeniden bağlanma denemesi, script sonlandırılıyor.[/bold red]") # By Rayzer

asyncio.run(keep_online(token)) # By Rayzer

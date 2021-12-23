from pytube import YouTube
import PySimpleGUI as sg
import os

class DownloaderYT:

    def __init__(self):

        sg.change_look_and_feel('LightGray1')

        layout =[
        
            [sg.Text('Link do video: ',size=(10,0)),sg.Input(size=(30,1),key='linkss')],
            [sg.Text('Diretorio onde deseja salvar: ',size=(10,0)),sg.Input(size=(30,1),key='local')],
            [sg.Text('Exemplo: C:\\\gsgomes\\\ytVideos \n  \n(Usar duas contra-barras para separar os diretorios)',size=(40,0))],
            [sg.Text('Caso o diretorio não seja informado, o arquivo sera salva em C:/ytvideos',size=(40,0))],
            [sg.Button('Fazer Download')]

       #    [sg.Output(size=(30,20))]
        ]

        self.janela = sg.Window("Downloader Videos YT").layout(layout)

    def Iniciar(self):

        # Mostra da onde as informacoes serao extraidas
            self.button, self.values = self.janela.Read()

        # Variaveis para cada chave: variavel = self.values['chaveDesejada']
            linkss = self.values['linkss']

            local = self.values['local']

            if local == "":

                mydir='C:\\ytVideos'


                if os.path.isdir(mydir):
                    print('Diretorio já criado')
                else:
                    print('Aguarde, um momento, o diretorio está sendo criado')
                    dir = 'C:\\ytVideos'
                    os.mkdir(dir)

            local = 'C:\\ytVideos'
            link = linkss
            path = local

        #   path = "C:\\gsgomes\\ytVideos"
            yt = YouTube(link)

#Mostra os detalhes do video

            print(f"Link do video: {linkss}")
            print(f"Local do arquivo: {local}")
            print("")
            print("Titulo", yt.title)
            print("Numero de views", yt.views)
            print("Tamanho do video", yt.length, "segundos")
            print("Avaliacao do video: ", yt.rating)


# Usa a maior resolucao
            ys = yt.streams.get_highest_resolution()

#Comeca o Download do video
            print("Baixando...")
            ys.download(path)
            print("Domload completo!")


tela = DownloaderYT()
tela.Iniciar()
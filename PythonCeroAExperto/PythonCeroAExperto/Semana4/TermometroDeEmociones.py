def TermometroDeEmociones():
    AngryEmotions = ["enojado", "aterrorizado", "estresado", "furioso", "celoso", "agitado", "disgutado"]
    WorriedEmotions = ["preocupado", "confundido", "avergonzado", "irritado", "nervioso", "frustrado"]
    HappyEmotions = ["feliz", "tranquilo", "orgulloso", "confiado", "enfocado", "pacifico", "dispuesto"]
    SadEmotions = ["triste", "decepcionado","solitario","enfermo","cansado", "aburrido", "timido"]
     
    SadSolutions = ["salir a caminar", "escuchar música relajante"]
    
    print("Bienvenido al Termometro de Emociones")
        
    while True:
        emocion = input("Por favor, dime cómo te sientes: ")

        if emocion.lower() in AngryEmotions:
            print("Estás experimentando emociones de enojo.")
            break
        elif emocion.lower() in WorriedEmotions:
            print("Estás experimentando emociones de preocupación.")
            break
        elif emocion.lower() in HappyEmotions:
            print("Estás experimentando emociones de felicidad.")
            break
        elif emocion.lower() in SadEmotions:
            print("Estás experimentando emociones de tristeza, para estos casos te recomiendo:")
            for solution in SadSolutions:
                print(solution)
            break
        else:
            print("Intenta describir tu estado de animo en una palabra")

TermometroDeEmociones()

    
    
filmes={
    "Drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela", "Clube da Luta", "O Pianista"],
    "Comédia": ["Tempos Modernos","American Pie","Dr. Dolittle", "Se Beber, Não Case!", "As Branquelas"],
    "Policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos", "Bad Boys 4", "Tropa de Elite"],
    "Guerra": ["Rambo","1917","Até o Último Homem", "12 Homens e uma Sentença", "O Resgate do Soldado Ryan"],
    "Anime": ["Bleach", "One Piece", "Dragon Ball", "Naruto", "Jujutsu Kaisen"],
    "Terror": ["Invocacao do Mal", "O Chamado", "It a coisa", "Terrifier", "Corra!"],
    "Romance": ["Como Eu Era Antes de Você", "A Culpa é das Estrelas", "Titanic", "Antes do Amanhecer", "Um Amor para Recordar"],
    "Ação": ["John Wick","Gladiador", "Matrix", "Kingsman: Serviço Secreto", "Top Gun: Maverick"],
    "Herói": ["Homem Aranha longe de casa", "Vingadores:Ultimato", "Superman(2025)", "Deadpool 3", "O Espetacular Homem-Aranha"]
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
            <style>
             
            <style>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()
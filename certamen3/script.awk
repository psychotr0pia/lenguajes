function crearIndexInvertido(url, texto) {
    # separar el texto en tokens
    split(texto, tokens, " ")
    # crear el index invertido
    for (i = 1; i <= length(tokens); i++) {
        token = tolower(tokens[i])
        if (!(token in indexInvertido)) {
            indexInvertido[token] = url
        } else {
            indexInvertido[token] = indexInvertido[token] "" url
        }
    }
}

# lee cada linea de gov2_pages.dat
{
    # encontramos el ultimo || de la linea
    ultimoSeparador = length($0)
    while (ultimoSeparador > 0 && substr($0, ultimoSeparador - 1, 2) != "||") {
        ultimoSeparador--
    }

    # separamos la url del texto
    url = substr($0, 1, ultimoSeparador - 1)
    texto = substr($0, ultimoSeparador + 1)
    gsub(/\|\|/, ".", url)

    # Build the inverted index for the current document
    crearIndexInvertido(url, texto)

}

# usando > indexInvertido.txt al final, esta se imprime a ese archivo
END {
    for (token in indexInvertido) {
        print token, indexInvertido[token]
    }
    printf "\n"  # Print a newline after the progress bar
}

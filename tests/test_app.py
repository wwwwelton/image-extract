from chalice.test import Client
from app import app

# https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg


def test_mensagens_de_bom_dia():
    with Client(app) as client:
        result = client.lambda_.invoke(
            'first_function', {'URL': 'https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg'})
        expected_str = str.encode(
            'Good morning!\nMay your day be light\nand full of smiles.', "utf-8")
        assert result.payload == {'Texto da imagem traduzido para o ingles': expected_str}


def test_sigmund_freud():
    with Client(app) as client:
        result = client.lambda_.invoke(
            'first_function', {'URL': 'https://cdn.pensador.com/img/frase/si/gm/sigmund_freud_minha_cultura_e_minhas_conquistas_sao_ale_trf_lqvg98e.jpg'})
        expected_str = str.encode('My culture and my\nAchievements are German.\nIntellectually\nI considered myself German until\nrealize that the\nantisemitic prejudices\nwere increasing in\nGermany and Austria. A\ngo away, leave me\nconsider german. I prefer\ndefine myself as a Jew.\n66 Baa tne Sigmund Freud', "utf-8")
        assert result.payload == {'Texto da imagem traduzido para o ingles': expected_str}


def test_italian_phrase():
    with Client(app) as client:
        result = client.lambda_.invoke(
            'first_function', {'URL': 'https://i.pinimg.com/236x/cf/7e/da/cf7eda50793451d65a4b098ac0771992.jpg'})
        expected_str = str.encode('To see the real face\nof a person you just have to\nwait for the time\nconsume the mask that\nwears.\nAmey', "utf-8")
        assert result.payload == {'Texto da imagem traduzido para o ingles': expected_str}

def test_italian():
    with Client(app) as client:
        result = client.lambda_.invoke(
            'first_function', {'URL': 'https://www.delcampe.net/static/img_large/auction/001/627/557/137_002.jpg?v=1'})
        expected_str = str.encode('YOU COME DOWN FROM THE STARS\nYou come down from the stars,\no King of heaven,\nand come to a cave\nin the cold and frost.\n\u00a9 My divine child,\n10 I see you here trembling.\nO blessed God!\nAh, how much it cost you\nhaving loved me.\nTo you who are of the world\nthe creator\nclothes and fire are missing,\nOh my Lord.\nDear elected little boy\nhow much this poverty\nthe more I fall in love\njackets made you love\nstill poor.\nGuido Reni, Adoration of the Shepherds\nwww.delcampe.net\norchard', "utf-8")
        assert result.payload == {
            'Texto da imagem traduzido para o ingles': expected_str}

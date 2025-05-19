import streamlit  as st

def hello_world():
    return "Olá turma de dados! Aula de Docker"

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()
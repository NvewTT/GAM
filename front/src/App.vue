<template>
  <div id="loginScreen">
        <div class="header">
            <h1>Bem vindo</h1>
            <p>Acesse sua conta</p>
        </div>
        <div class="login">
            <h1>Acesse sua conta</h1>
            <form action="">
                <input type="text" placeholder="Nome">
                <input type="password" placeholder="Senha">
                <button class="submit">Entrar</button>
                <a class="button-link" href="/recover.html">Recuperar Senha</a>
            </form>
        </div>
        
    </div>
</template>

<script>
export default {
  methods: {
    mostrarRouter() {
      console.log(this.$route);
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
body {
  font-family: "Poppins", sans-serif;
  margin: 0;
  padding: 0;
}

#loginScreen {
  background-color: #EEF0F2;
  height: 100vh;
  display: flex;
  position: relative;
}
@media (max-width: 600px) {
  #loginScreen {
    flex-wrap: wrap;
  }
}
#loginScreen .header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #0D1F22;
  color: white;
  padding: 50px;
  width: 100%;
  max-width: 350px;
  text-align: center;
}
@media (max-width: 600px) {
  #loginScreen .header {
    max-width: 100%;
  }
}
#loginScreen .header h1 {
  margin-bottom: 40px;
}
#loginScreen .login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  padding: 50px;
}
#loginScreen .login h1 {
  text-align: center;
  color: #0D1F22;
  margin-bottom: 60px;
}
#loginScreen .login form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#loginScreen .login form input {
  width: 100%;
  max-width: 450px;
  background-color: transparent;
  border: 2px solid #0D1F22;
  border-radius: 15px;
  color: #0D1F22;
  padding: 10px 20px;
  margin-bottom: 15px;
}
#loginScreen .login form input::-moz-placeholder {
  font-size: 13px;
}
#loginScreen .login form input:-ms-input-placeholder {
  font-size: 13px;
}
#loginScreen .login form input::placeholder {
  font-size: 13px;
}
#loginScreen .login form .submit {
  background-color: #0D1F22;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 15px;
  font-weight: bold;
}
#loginScreen .login form .button-link {
  background: none;
  color: #0D1F22;
  border: none;
  margin-top: 20px;
  font-size: 13px;
}

</style>

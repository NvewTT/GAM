<template>
  <div id="passwordScreen">

        <div class="recover">
            <h1>Recupere sua senha</h1>
            <p>Sua senha será enviada para seu email</p>
            <form action="">
                <input type="email" placeholder="Email">
                <button class="submit">Recuperar</button>
            </form>

        </div>
    </div>
</template>

<script>
export default {};
</script>

<style>
#passwordScreen .recover {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 50px;
}
#passwordScreen .recover h1 {
  text-align: center;
  color: #0D1F22;
  margin-bottom: 60px;
}
#passwordScreen .recover p {
  text-align: center;
  margin-bottom: 60px;
}
#passwordScreen .recover form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#passwordScreen .recover form input {
  width: 100%;
  max-width: 450px;
  background-color: transparent;
  border: 2px solid #0D1F22;
  border-radius: 15px;
  color: #0D1F22;
  padding: 10px 20px;
  margin-bottom: 60px;
}
#passwordScreen .recover form input::-moz-placeholder {
  font-size: 13px;
}
#passwordScreen .recover form input:-ms-input-placeholder {
  font-size: 13px;
}
#passwordScreen .recover form input::placeholder {
  font-size: 13px;
}
#passwordScreen .recover form .submit {
  background-color: #0D1F22;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 15px;
  font-weight: bold;
}

</style>

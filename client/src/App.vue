<template>
  <!-- <div id="nav">
    <router-link to="/">Survey</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <router-view />
  <div class="footer">© 2021 Carleton Computer Science Society</div>
</template>

<style lang="scss">
body {
  padding: 0;
  margin: 0;
}

.survey-page {
  height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;

  .survey-complete-message {
    font-size: 32px;
    font-weight: 700;
  }
}

.footer {
  height: 10vh;
  background: black;
  color: white;
  display: flex;
  font-size: 0.9rem;
  justify-content: center;
  align-items: center;
  border-top: 3px solid #c40729;
}

#app {
  font-family: "Source Sans Pro", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
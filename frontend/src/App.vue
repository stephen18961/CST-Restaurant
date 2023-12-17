<template>
  <div class="container app">

    <div class="row">
      <div class="col-2">
        <nav>
          <router-link to="/">Home</router-link> |
          <router-link to="/menu">Menu</router-link> |
          <router-link to="/add">Add</router-link>
        </nav>
      </div>
      <div class="col-6">
        <router-view/>
      </div>
      <div class="col-4 border">
      <h4>#ORDER</h4>
      <div>
        Selected table: {{ selectedTable }}
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.app {
  max-width: 100% !important;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

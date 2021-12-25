<template>
  <div>
    <div id="nav">
      <router-link to="/">主页</router-link> |
      <router-link to="/read">读一封信</router-link> |
      <router-link to="/write">写一封信</router-link> |
      <router-link to="/read_my_story">读读我诞生的故事</router-link>
    </div>
    <div id="container">
      <div class="show_page">
        <router-view/>
      </div>
    </div>
  </div>
</template>


<style>
.show_page {
  margin: auto;
  border-radius: 13px;
  background-color: #ffe4e1;
  opacity: 0.8;
  background-size: 22px 22px;
  min-width: 300px;
  max-width: 900px;
  position: relative;
  padding-top: 20px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 20px;
  text-align: left;
  border-right: 2px dotted #f78da7;
  border-left: 2px dotted #f78da7;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

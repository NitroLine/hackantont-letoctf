<template>
  <div class="common-layout">
    <el-container>
      <el-header class="row">
        <img class="logo" alt="Vue logo" src="./assets/logo.png">
        <h2>SQLAB</h2>
      </el-header>
      <el-main>
        <router-view>

        </router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>


export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
.center{
  text-align:center;
}
.logo{
  max-width: 50px;
}
.row{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

<template>
  <div id="app">
    <BlockChain />
  </div>
</template>

<script>
import BlockChain from './components/BlockChain.vue'

export default {
  name: 'App',
  components: {
    BlockChain
  }
}
</script>

<style>
body {
  margin: 0;
  height: 100vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0;
}
</style>

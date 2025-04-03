<template>
  <div id="app">
    <input v-model="query" @input="search" placeholder="Buscar operadora">
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.id_operadora">
        {{ operadora.nome }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
      operadoras: []
    }
  },
  methods: {
    search() {
      this.$http.get(`http://localhost:5000/search?query=${this.query}`)
        .then(response => {
          this.operadoras = response.data
        })
    }
  }
}
</script>

<style>
/* Adicionar os estilos aqui */
</style>
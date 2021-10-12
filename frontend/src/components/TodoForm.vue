<template>
  <div class="w-2/4 mx-auto mt-10 grid grid-cols-5 gap-x-2 grid-flow-row">
    <input type="text" v-model="msg" class="col-span-4 block w-full border-1" @keyup.enter="addTask">
    <button @click="addTask" class="p-2 text-white bg-green-500">+</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TodoForm',
  emits: ['updateTask'],
  data() {
    return {
      msg: null,
    }
  },
  methods: {
    async addTask() {
      await axios
          .post('http://127.0.0.1:8000/api/v1/task/create/',{content: this.msg})
          .then(response => (response))
          .catch(error => (console.log(error)))
      this.msg = ''
      this.$emit('updateTask')
    }
  }
}
</script>

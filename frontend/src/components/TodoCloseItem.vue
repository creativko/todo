<template>
  <div class="w-2/4 mx-auto grid grid-cols-5 gap-x-2 grid-flow-row bg-green-200 p-4 mt-2" v-for="task in taskList" :key="task.id">
    <div class="text-black font-mono col-span-4">
      {{ task.content }}
    </div>
    <div class="flex flex-wrap">
      <button @click="deletedTask(task.id)" class="bg-red-600 font-mono text-center p-2 text-white w-full hover:bg-red-400 transition">удалить</button>
    </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: 'TodoItem',
  emits: ['taskDeleted'],
  props: {
    taskList: {
      type: Object,
      required: true
    }
  },
  methods: {
    async deletedTask(taskId) {
      await axios
          .delete(`http://127.0.0.1:8000/api/v1/task/${taskId}/delete/`)
          .catch(error => (error))
      this.$emit('taskDeleted')
    }
  }
}
</script>

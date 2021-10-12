<template>
  <div class="container mx-auto">
    <h2 class="text-center text-xl font-semibold uppercase pt-8 text-gray-600 font-mono">Список задач</h2>
    <TodoForm @updateTask="updateTask" />
    <h2 class="text-center text-xl font-semibold uppercase pt-8 text-gray-600 font-mono">Открытые задачи</h2>
    <template v-if="taskList.length > 0">
      <TodoItem @taskDeleted="updateTask" @taskClose="updateTask" @closeTaskItem="filterTask" :taskList="taskList" />
    </template>
    <template v-else>
      <h3 class="text-center text-sm font-semibold uppercase pt-8 text-gray-600 font-mono">Открытых задач нет!</h3>
    </template>
    <h2 class="text-center text-xl font-semibold uppercase pt-8 text-gray-600 font-mono">Закрытие задачи</h2>
    <TodoCloseItem @taskDeleted="filterTask" :taskList="taskFilterList" />
  </div>
</template>

<script>
import axios from 'axios';

import TodoItem from '../components/TodoItem.vue'
import TodoForm from '../components/TodoForm.vue'
import TodoCloseItem from '../components/TodoCloseItem.vue'

export default {
  name: 'TodoList',
  data() {
    return {
      taskList: [],
      taskFilterList: []
    }
  },
  components: {
    TodoItem,
    TodoForm,
    TodoCloseItem
  },
  mounted() {
    this.updateTask()
    this.filterTask()
  },
  methods: {
    updateTask() {
      axios.get('http://127.0.0.1:8000/api/v1/task/list/')
      .then(response => (this.taskList = response.data.filter(item => item.status === 'open')))
    },
    filterTask() {
      axios.get('http://127.0.0.1:8000/api/v1/task/list/')
      .then(response => (this.taskFilterList = response.data.filter(item => item.status === 'close')))
    }
  },
}
</script>

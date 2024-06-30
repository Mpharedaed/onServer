<template>
    <b-container>
      <b-row>
        <b-col>
          <b-list-group>
            <b-list-group-item v-for="user in users" :key="user.id" @click="selectUser(user)">
              {{ user.username }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script>
  export default {
    name: 'UserList',
    props: {
      users: {
        type: Array,
        required: true
      }
    },
    methods: {
      selectUser(user) {
        this.$emit('select-user', user);
      }
    }
  }
  </script>
  
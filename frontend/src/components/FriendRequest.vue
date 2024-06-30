<template>
    <b-container>
      <b-row>
        <b-col cols="4">
          <UserList :users="users" @select-user="selectUser" />
        </b-col>
        <b-col cols="8">
          <UserProfile v-if="selectedUser" :user="selectedUser" />
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script>
  import UserList from '@/components/UserList.vue';
  import UserProfile from '@/components/UserProfile.vue';
  import axios from '@/plugins/axios';
  
  export default {
    name: 'FriendRequest',
    components: {
      UserList,
      UserProfile
    },
    data() {
      return {
        users: [],
        selectedUser: null
      };
    },
    created() {
      this.fetchUsers();
    },
    methods: {
      fetchUsers() {
        axios.get('/users')
          .then(response => {
            this.users = response.data.users;
          })
          .catch(error => {
            console.error('There was an error fetching users!', error);
          });
      },
      selectUser(user) {
        this.selectedUser = user;
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  
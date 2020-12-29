<template>
<div class="container">
    <b-row>
      <b-col cols="10">
        <b-row>
          <b-table :items="posts" :fields="fields" responsive primary-key="id">
            <template v-slot:cell(title)="data">
              <p><b-link :to="{ name: 'retrieve-post', params: { id: data.item.id } }">{{ data.item.title }}</b-link></p>
            </template>
            <template v-slot:cell(owner)="data">
              <p>{{ data.item.owner.email }}</p>
            </template>
          </b-table>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "postList",
  props: ['posts'],
  data() {
    return {
      fields: [
        'title',
        'created',
        'modified',
        'owner',
        'users_liked_count'
      ],
    };
  },
}
</script>
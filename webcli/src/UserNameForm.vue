<template>
    <v-card>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field label="User name" v-model="UserName" required></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="onNext">Next</v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
export default {
  name: 'UserNameForm',
  methods: {
      onNext() {
        this.$emit('UserNameCollected', this.UserName);
      }
  },
  props: ['DefaultUserName'],
  data: function(){
      return {
          UserName: this.DefaultUserName
    }
  }
};
</script>

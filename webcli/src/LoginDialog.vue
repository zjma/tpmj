<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field label="您的昵称:" v-model="UserName" required></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" large text @click="onNext"><v-icon>mdi-arrow-right</v-icon></v-btn>
          </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    name: 'LoginDialog',
    methods: {
        onNext() {
            this.$emit('finished', this.UserName);
        }
    },
    props: {
        active          : Boolean,
        defaultUserName : String
    },
    data: function(){
        return {
            UserName: this.defaultUserName
        }
    }
};
</script>

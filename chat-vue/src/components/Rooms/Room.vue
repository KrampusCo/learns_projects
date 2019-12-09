<template>
	<mu-col span="4" xl="2">
		<h1> Your Room</h1>
		<div v-for="room in rooms" class="room-list">
					<h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
					{{room.date}}
		</div>			
	</mu-col>
</template>

<script>
	import $ from 'jquery'
	

	export default{
		name:"Room",
		data() {
			return{
				rooms:'',
			}
		},
		
		created() {
			$.ajaxSetup({
				headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")},
			});
			this.loadRoom()
		},
		methods: {
			loadRoom(){
				$.ajax({
					url: "http://localhost:8000/api/v1/chat/rooms/",
					type: "GET",
					success: (response)=>{
						this.rooms=response.data.data
						console.log(response)
					}
				})
			},
			openDialog(id){
				this.$emit('openDialog', id)
			},
		}
	}
</script>

<style scoped>
	.room-list{
		margin: 0 10px 0  0;
		box-shadow: 1px 2px 1px 3px #cccccc;
	}
</style>

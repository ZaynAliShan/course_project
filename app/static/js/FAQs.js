function deleteFAQ(id)
{
  fetch(`${window.origin}/delete_faq`, {
    method: "POST",
    body: JSON.stringify({id: id}),
    headers:{
      "Content-Type":"application/json"
    }
  })
  .then(
    location.reload()
  )
  // .then(data => {
  //   if (data.success)
  //   {
  //     console.log("Delete Successfully");
  //   }
  // })
  // .catch(error => {
  //   console.error("ERROR:", error);
  // });
}

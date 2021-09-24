function search_snippet(event){
    var snipped_id = document.getElementById('snippet_id').value;
    console.log(snipped_id);
    window.location.replace("/snippets/page/"+snipped_id)
}
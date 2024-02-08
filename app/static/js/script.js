async function comentar(id, user_id) {
  const { value: text } = await Swal.fire({
    input: "textarea",
    inputLabel: "Comentário",
    inputPlaceholder: "Escreva aqui o seu comentário...",
    inputAttributes: {
      "aria-label": "Type your message here",
    },
    showCancelButton: true,
    confirmButtonText: "Salvar",
    cancelButtonText: "Cancelar",
  });
  if (text) {
    const response = await fetch("/comment/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        post_id: id,
        user_id: user_id,
        text: text,
      }),
    });

    if (response.ok) {
      Swal.fire("Comentário enviado com sucesso!");
      setTimeout(function () {
        window.location.reload();
      }, 3000);
    } else {
      Swal.fire("Erro ao enviar o comentário. Tente novamente.");
    }
  }
}

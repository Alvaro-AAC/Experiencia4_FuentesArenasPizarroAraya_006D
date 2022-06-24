def total_carro(request):
    total = 0
    if 'usuario' in request.session:
        try:
            for key, value in request.session["carro"].items():
                total = total+int(value["precio"])
        except KeyError:
            request.session['carro']={}
            total = 0
    return {"total_carro":total}
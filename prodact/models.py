from django.db import models
from django.utils.translation import gettext_lazy as _
class Categore (models.Model) :
    parinrt = models.ForeignKey('self', verbose_name=_('parint'), blank= True, null= True, on_delete=models.CASCADE)
    timeit = models.CharField(_('title'),max_length=60)
    description = models.Transform(_('description'),blank = True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='Categore/')
    is_enble = models.BooleanField(_('is_enble'),default=True)
    creat_time = models.DateTimeField(_('creat_time'),auto_now_add=True)
    updat_time = models.DateTimeField(_('uplod_time'),auto_now=True)

    class mata :
        db_table = _(' Categore')
        vrbos_name = _(' Categore')
        vrbosname_plus = _(' Categore')

class Prodact (models.Model) :
    timeit = models.CharField(_('title'),max_length=60)
    description = models.Transform(_('description'),blank = True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='prodqct/')
    is_enble = models.BooleanField(_('is_enble'),default=True)
    categoris = models.ManyToManyField('Categore',verbose_name=_(' Categore'),blank= True)
    creat_time = models.DateTimeField(_('creat_time'),auto_now_add=True)
    updat_time = models.DateTimeField(_('uplod_time'),auto_now=True)
    class mate  :
        db_table = 'prodact'
        vrbos_name = _('prodact')
        vrbosname_plus = _('prodact')

class Fali (models.Model) :
    parinrt = models.ForeignKey('prodact',verbose_name=_('parint'), on_delete=models.CASCADE)
    file = models.FileField(_('file'),upload_to='file/%Y/%m/%d/')
    timeit = models.CharField(_('title'),max_length=60)
    is_enble = models.BooleanField(_('is_enble'),default=True)
    creat_time = models.DateTimeField(_('creat_time'),auto_now_add=True)
    updat_time = models.DateTimeField(_('uplod_time'),auto_now=True)
    class mate  :
        db_table = 'file'
        vrbos_name = _('flie')
        vrbosname_plus = _('file')
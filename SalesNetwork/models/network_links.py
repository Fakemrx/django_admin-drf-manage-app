from django.db import models
from SalesNetwork.models.additional_information import SellersNetwork


class Factory(models.Model):
    info = models.ForeignKey(SellersNetwork, on_delete=models.CASCADE,
                             related_name='factory_info_set', db_index=True, null=False, blank=False,
                             verbose_name='Завод')

    @property
    def get_provider(self):
        return None

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'Завод "{self.info.name}"'


class Distributor(models.Model):
    info = models.ForeignKey(SellersNetwork, on_delete=models.CASCADE,
                             related_name='distributor_info_set', db_index=True, null=False, blank=False,
                             verbose_name='Дистрибьютор')
    factory_provider = models.ForeignKey(Factory, on_delete=models.deletion.SET_NULL,
                                 related_name='fact_to_dist_set', db_index=True, null=True, blank=True,
                                 verbose_name='Поставщик <Завод>')

    @property
    def get_provider(self):
        if self.factory_provider is not None:
            return self.factory_provider

    class Meta:
        verbose_name = 'Дистрибьютор'
        verbose_name_plural = 'Дистрибьюторы'

    def __str__(self):
        return f'Дистрибьютор "{self.info.name}"'


class Dealership(models.Model):
    info = models.ForeignKey(SellersNetwork, on_delete=models.CASCADE,
                             related_name='dealership_info_set', db_index=True, null=False, blank=False,
                             verbose_name='Дилерский центр')
    factory_provider = models.ForeignKey(Factory, on_delete=models.deletion.SET_NULL,
                                 related_name='fact_to_deal_set', db_index=True, null=True, blank=True,
                                 verbose_name='Поставщик <Завод>')
    distributor_provider = models.ForeignKey(Distributor, on_delete=models.deletion.SET_NULL,
                                 related_name='dist_to_deal_set', db_index=True, null=True, blank=True,
                                 verbose_name='Поставщик <Дистрибьютор>')

    @property
    def get_provider(self):
        if self.factory_provider is not None:
            return self.factory_provider
        elif self.distributor_provider is not None:
            return self.distributor_provider

    class Meta:
        verbose_name = 'Дилерский центр'
        verbose_name_plural = 'Дилерские центры'

    def __str__(self):
        return f'Дилерский центр "{self.info.name}"'


class Retailer(models.Model):
    info = models.ForeignKey(SellersNetwork, on_delete=models.CASCADE,
                             related_name='retailer_info_set', db_index=True, null=False, blank=False,
                             verbose_name='Крупная розничная сеть')
    factory_provider = models.ForeignKey(Factory, on_delete=models.deletion.SET_NULL,
                                         related_name='fact_to_ret_set', db_index=True, null=True, blank=True,
                                         verbose_name='Поставщик <Завод>')
    distributor_provider = models.ForeignKey(Distributor, on_delete=models.deletion.SET_NULL,
                                             related_name='dist_to_ret_set', db_index=True, null=True, blank=True,
                                             verbose_name='Поставщик <Дистрибьютор>')
    dealership_provider = models.ForeignKey(Dealership, on_delete=models.deletion.SET_NULL,
                                         related_name='deal_to_ret_set', db_index=True, null=True, blank=True,
                                         verbose_name='Поставщик <Дилерский центр>')

    @property
    def get_provider(self):
        if self.factory_provider is not None:
            return self.factory_provider
        elif self.distributor_provider is not None:
            return self.distributor_provider
        elif self.dealership_provider is not None:
            return self.dealership_provider

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return f'Розничная сеть "{self.info.name}"'


class IndividualSeller(models.Model):
    info = models.ForeignKey(SellersNetwork, on_delete=models.CASCADE,
                             related_name='sellers_info_set', db_index=True, null=False, blank=False,
                             verbose_name='ИП')
    factory_provider = models.ForeignKey(Factory, on_delete=models.deletion.SET_NULL,
                                         related_name='fact_to_ind_set', db_index=True, null=True, blank=True,
                                         verbose_name='Поставщик <Завод>')
    distributor_provider = models.ForeignKey(Distributor, on_delete=models.deletion.SET_NULL,
                                             related_name='dist_to_ind_set', db_index=True, null=True, blank=True,
                                             verbose_name='Поставщик <Дистрибьютор>')
    dealership_provider = models.ForeignKey(Dealership, on_delete=models.deletion.SET_NULL,
                                            related_name='deal_to_ind_set', db_index=True, null=True, blank=True,
                                            verbose_name='Поставщик <Дилерский центр>')
    retailer_provider = models.ForeignKey(Dealership, on_delete=models.deletion.SET_NULL,
                                            related_name='ret_to_ind_set', db_index=True, null=True, blank=True,
                                            verbose_name='Поставщик <Розничная сеть>')

    @property
    def get_provider(self):
        if self.factory_provider is not None:
            return self.factory_provider
        elif self.distributor_provider is not None:
            return self.distributor_provider
        elif self.dealership_provider is not None:
            return self.dealership_provider
        elif self.retailer_provider is not None:
            return self.retailer_provider

    class Meta:
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'

    def __str__(self):
        return f'ИП "{self.info.name}"'

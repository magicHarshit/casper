__author__ = 'harshit'

from model_i18n import translator

from models import WallPost


class ItemTranslation(translator.ModelTranslation):
    fields = ('title',)
    db_table = 'item_translation'


translator.register(WallPost, ItemTranslation)


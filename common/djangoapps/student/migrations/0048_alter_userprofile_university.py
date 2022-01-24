# Generated by Django 3.2.11 on 2022-01-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0047_auto_20220117_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='university',
            field=models.CharField(blank=True, choices=[('1', 'Ada Universiteti'), ('2', 'Azərbaycan Əmək və Sosial Münasibətlər Akademiyası'), ('3', 'Azərbaycan Milli Konservatoriyası'), ('4', 'Azərbaycan\xa0Dillər\xa0Universiteti'), ('5', 'Azərbaycan\xa0Dövlət\xa0Aqrar\xa0Universiteti'), ('7', 'Azərbaycan\xa0Dövlət\xa0Bədən\xa0Tərbiyəsi\xa0və\xa0İdman\xa0Akademiyası\xa0'), ('8', 'Azərbaycan\xa0Dövlət\xa0Dəniz\xa0Akademiyası\xa0'), ('9', 'Azərbaycan\xa0Dövlət\xa0İqtisad\xa0Universiteti'), ('10', 'Azərbaycan\xa0Dövlət\xa0Mədəniyyət\xa0və\xa0İncəsənət\xa0Universiteti'), ('11', 'Azərbaycan\xa0Dövlət\xa0Neft\xa0və\xa0Sənaye\xa0Universiteti'), ('12', 'Azərbaycan\xa0Dövlət\xa0Pedaqoji\xa0Universiteti'), ('13', 'Azərbaycan\xa0Dövlət\xa0Rəssamlıq\xa0Akademiyası\xa0'), ('14', 'Azərbaycan\xa0İlahiyyat\xa0İnstitutu'), ('15', 'Azərbaycan\xa0Kooperasiya\xa0Universiteti'), ('16', 'Azərbaycan\xa0Memarlıq\xa0və\xa0İnşaat\xa0Universiteti'), ('17', 'Azərbaycan\xa0Milli\xa0Elmlər Akademiyası'), ('18', 'Azərbaycan\xa0Respublikası\xa0Prezidenti\xa0yanında\xa0Dövlət\xa0İdarəçilik\xa0Akademiyası'), ('19', 'Azərbaycan\xa0Respublikasının\xa0Təhsil\xa0İnstitutu'), ('20', 'Azərbaycan\xa0Respublikasının\xa0Təhsil\xa0Nazirliyi'), ('21', 'Azərbaycan\xa0Texniki\xa0Universiteti'), ('22', 'Azərbaycan\xa0Texnologiya\xa0Universiteti'), ('23', 'Azərbaycan\xa0Tibb\xa0Universiteti\xa0'), ('24', 'Azərbaycan\xa0Turizm\xa0və\xa0Menecment\xa0Universiteti'), ('25', 'Azərbaycan\xa0Universiteti'), ('26', 'Bakı İslam Universiteti'), ('27', 'Bakı\xa0Ali Neft\xa0Məktəbi\xa0'), ('28', 'Bakı\xa0Avrasiya\xa0Universiteti'), ('29', 'Bakı\xa0Biznes\xa0Universiteti'), ('30', 'Bakı\xa0Dövlət\xa0Universiteti'), ('31', 'Bakı\xa0Mühəndislik\xa0Universiteti'), ('32', 'Bakı\xa0Musiqi\xa0Akademiyası\xa0'), ('33', 'Bakı\xa0Qızlar\xa0Universiteti'), ('34', 'Bakı\xa0Slavyan\xa0Universiteti'), ('35', 'Bakı\xa0Xoreoqrafiya\xa0Akademiyası'), ('36', 'Gəncə\xa0Dövlət\xa0Universiteti'), ('37', 'İ. M.\xa0Seçenov\xa0adına\xa0Birinci Moskva\xa0Dövlət\xa0Tibb\xa0Universitetinin\xa0Bakı\xa0filialı\xa0'), ('38', 'Lənkəran\xa0Dövlət\xa0Universiteti'), ('39', 'M. V. Lomonosov\xa0adına\xa0Moskva\xa0Dövlət\xa0Universitetinin\xa0Bakı\xa0filialı'), ('40', 'Milli\xa0Aviasiya\xa0Akademiyası'), ('41', 'Mingəçevir\xa0Dövlət\xa0Universiteti'), ('42', 'Naxçıvan\xa0Dövlət\xa0Universiteti'), ('43', 'Naxçıvan Müəllimlər İnstitutu'), ('44', 'Naxçıvan Müəllimlər İnstitutu'), ('45', 'Naxçıvan\xa0Universiteti\xa0'), ('46', 'Odlar Yurdu Universiteti'), ('47', 'Qərbi\xa0Kaspi\xa0Universiteti'), ('48', 'Sumqayıt\xa0Dövlət\xa0Universiteti'), ('49', 'Xəzər\xa0Universiteti\xa0'), ('50', 'Digər')], default=0, max_length=2, null=True),
        ),
    ]

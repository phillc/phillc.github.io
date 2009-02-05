
    @permalink
    def get_absolute_url(self):
        return ('blog_entry', (),
            {
                'sectionSlug' : str(self.section.slug),
                'year'        : str(self.publish.year),
                'month'       : str(self.publish.strftime('%b')).lower(),
                'day'         : str(self.publish.day).zfill(2),
                'slug'        : str(self.slug),
            },
        )

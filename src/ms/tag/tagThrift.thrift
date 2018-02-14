service TagThrift {
    list<string> getTag(1:string tag_id),
    list<string> addTag(1:string name),
    list<string> deleteTag(1:string tag_id),
    list<string> getTags(1:string beginTag),
    void deleteAllTags(),
}

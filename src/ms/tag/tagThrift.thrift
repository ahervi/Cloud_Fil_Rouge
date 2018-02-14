service TagThrift {
    bool addTag(1:string tag),
    string deleteTag(1:string tag),
    list<string> getTags(1:string beginTag),
}
